import os

from flask import Flask

from config import app_config


def create_app(config_name='development'):
    if os.getenv('FLASK_ENV') == 'production':
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    from .api.index import index as index_blueprint
    app.register_blueprint(index_blueprint)

    return app
