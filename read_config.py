from configparser import ConfigParser
import psycopg2

def config(filename = 'database.cfg', section = 'DATABASE'):
    parser = ConfigParser()
    parser.read(filename)

    database = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            database[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file.'.format(section, filename))
    return database

def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        print('Connected to the PostgreSQL database...')
    except:
        print('Not connected to the PostgreSQL database...')
    return conn