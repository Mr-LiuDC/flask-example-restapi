import os

from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/'), 'flask-icon.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run()
