from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/')
def index():
    return "This route will contain all auth routes"
