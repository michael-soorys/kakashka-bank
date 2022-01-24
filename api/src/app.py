
import os
import time

from dotenv import dotenv_values, load_dotenv
from flask import Flask
from flask_pymongo import pymongo

from config import Config

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
env = dotenv_values(dir_path + '/.env')

config = Config.getConfig(app.config['ENV'])

# Connect to database
connection_string = env['MONGO_URI']
client = pymongo.MongoClient(connection_string)
db = client.get_database('main')
userData = pymongo.collection.Collection(db, config['dbCollection'])

# Initialize the starter document if missing





@app.route("/")
def hello_world():
    userData.insert_one({'test2':'malachi smells'})
    return "<p>Hello, World!</p>"
    
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == "__main__":
    app.run()
