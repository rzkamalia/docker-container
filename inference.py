from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import os
import datetime

from log import *

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD'] = upload_folder

class_names = ['2nd generation group', '1st generation group']

def main(img):
    # process AI
    model = tf.keras.models.load_model('model50epoch.h5')
    img = tf.keras.utils.load_img(img)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # create a batch
    pred = model.predict(img_array)
    score = tf.nn.softmax(pred[0])
    classes = class_names[np.argmax(score)]
    confident = round(100 * np.max(score), 2)
    
    # time
    date_time = datetime.datetime.now()
    str_date_time = str(date_time.strftime('%Y-%m-%d %H:%M:%S'))

    # process database
    database_name = 'classification'
    variable_name = ['time', 'class', 'confident']
    variable_value = ["%s", "%s", "%s"]
    variable_name = ', '.join(variable_name)
    variable_value = ', '.join(variable_value)
    data_log = [str_date_time, classes, confident]

    create_table(database_name)
    insert_to_database(database_name, variable_name, variable_value, data_log)
    return classes, confident

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        classes, confident = main(img)
        return render_template('image_render.html', img = img, classes = classes, confident = confident)
    return render_template('image_render.html')
    
app.run(host = '0.0.0.0', port = 5000)
