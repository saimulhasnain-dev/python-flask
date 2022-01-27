from operator import methodcaller
from flask import Blueprint, jsonify
from db import db
auth = Blueprint('auth', __name__)


@auth.route('/', methods=["GET"])
def index():
    db.user.insert_one({"user": "dfdsf", "pass": "Rt"})
    return jsonify("This route will contain all auth routes",)
