from crypt import methods
from flask import Flask
from flask_pymongo import PyMongo

from auth.auth import auth
from user.user import user

app = Flask(__name__)


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(user, url_prefix="/user")


@app.route('/',methods=["GET"])
def index():
    return "This is an example app"


if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
