from flask import send_from_directory

from . import index


@index.route('/')
def hello_world():
    return 'Hello World!'


@index.route('/favicon.ico')
def favicon():
    return send_from_directory('static/', 'flask-icon.png', mimetype='image/png')
