from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/')
def index():
    return "This route will contain all user routes"
