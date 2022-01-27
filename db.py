from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb+srv://root:root@cluster0.kfepw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db