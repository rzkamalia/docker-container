from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import numpy as np
import cv2
import os
import datetime
import torch
import torchvision

from googlenet import *
from log import *
from read_config import *

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

app.config['UPLOAD'] = upload_folder

class_names = ['1st generation group', '2nd generation group']

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
model = GoogleNet(num_classes = 2)
weights = torch.load(weight)
model.load_state_dict(weights)
model.eval()
model.to(device)

def main(img):
    # process AI
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torchvision.transforms.ToTensor()(img)
    img = img[None] # expand for batch dim
    img = img.to(device)

    outputs = model(img)
    score = torch.nn.Softmax()(outputs)
    classes = class_names[torch.argmax(score)]
    confident = round(100 * torch.max(score).item(), 2)
    
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
