import datetime

from flask import request
from werkzeug.security import generate_password_hash

from app.models import User, UserSchema
from app.utils.rest_response import build_response
from . import user
from ... import db

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user.route('/api/user', methods=['POST'])
def create():
    request_data = request.get_json()
    user_info = User.create(request_data['username'], request_data['password'], request_data['email'])
    return build_response(user_schema.dump(user_info))


@user.route("/api/user/<user_id>", methods=['PUT'])
def update(user_id):
    request_data = request.get_json()
    user_info = User.query.get(user_id)
    if user_info:
        user_info.email = request_data['email']
        user_info.username = request_data['username']
        user_info.password_hash = generate_password_hash(request_data['password'])
        user_info.last_update_time = datetime.datetime.now()
        db.session.commit()
    return build_response(user_schema.dump(user_info))


@user.route("/api/user/<user_id>", methods=['DELETE'])
def delete_by_id(user_id):
    user_info = User.query.get(user_id)
    if user_info:
        db.session.delete(user_info)
        db.session.commit()
    return build_response(None, code=201, http_status=201)


@user.route("/api/user/<user_id>", methods=['GET'])
def get_by_id(user_id):
    user_info = User.query.get(user_id)
    return build_response(user_schema.dump(user_info))


@user.route('/api/user', methods=['GET'])
def list_all():
    user_list = User.query.all()
    return build_response(users_schema.dump(user_list))
