
import os

from dotenv import dotenv_values, load_dotenv
from flask import Flask
from flask_pymongo import pymongo

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
env = dotenv_values(dir_path + '/.env')

# Connect to database
connection_string = env['MONGO_URI']
client = pymongo.MongoClient(connection_string)
db = client.get_database('main')
userData = pymongo.collection.Collection(db, 'userData')

@app.route("/")
def hello_world():
    userData.insert_one({'test2':'malachi smells'})
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()
