from flask import request

from app.models import User
from app.utils.rest_response import build_response
from . import user


@user.route('/api/user', methods=['POST'])
def create():
    request_data = request.get_json()
    user_info = User.create(request_data['username'], request_data['password'], request_data['email'])
    return build_response(user_info)


@user.route("/api/user/<user_id>", methods=['PUT'])
def update(user_id):
    user_info = User.query.get(user_id)
    return build_response(user_info)


@user.route("/api/user/<user_id>", methods=['DELETE'])
def delete_by_id(user_id):
    user_info = User.query.get(user_id)
    return build_response(user_info)


@user.route("/api/user/<user_id>", methods=['GET'])
def get_by_id(user_id):
    user_info = User.query.get(user_id)
    return build_response(user_info)


@user.route('/api/user', methods=['GET'])
def list_all():
    user_list = User.query.all()
    return build_response(user_list)
