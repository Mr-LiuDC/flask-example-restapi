from flask import jsonify, make_response, request, Response

from app.models import User
from app.utils.rest_response import created
from . import user


@user.route('/api/user', methods=['POST'])
def create():
    request_data = request.get_json()
    response = Response("User added", 201, mimetype='application/json')

    return created("User added")


@user.route("/api/user/<user_id>", methods=['PUT'])
def update(user_id):
    user_info = User.query.get(user_id)
    return jsonify(user_info)


@user.route("/api/user/<user_id>", methods=['DELETE'])
def delete_by_id(user_id):
    user_info = User.query.get(user_id)
    return jsonify(user_info)


@user.route("/api/user/<user_id>", methods=['GET'])
def get_by_id(user_id):
    user_info = User.query.get(user_id)
    return jsonify(user_info)


@user.route('/api/user', methods=['GET'])
def list_all():
    user_list = User.query.all()
    # return make_response(jsonify(user_list), 200)
    return created(jsonify(user_list))
