from read_config import *

def create_table(database_name):
    conn = connect()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS " + database_name + " (time TIMESTAMP NOT NULL, class VARCHAR(255) NOT NULL, confident NUMERIC(10,2) NOT NULL)")
        cur.close()
        conn.commit()

def insert_to_database(database_name, variable_name, variable_value, data_log):
    conn = connect()
    if conn is not None:
        cur = conn.cursor()
        cur.execute("INSERT INTO " + database_name + "(" + variable_name + ") VALUES(" + variable_value + ");", (data_log))          
        cur.close()
        conn.commit()
        conn.close()