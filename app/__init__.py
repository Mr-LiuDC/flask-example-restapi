import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import app_config

db = SQLAlchemy()


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

    db.init_app(app)

    Migrate(app, db)

    from app import models

    from .api.index import index as index_blueprint
    app.register_blueprint(index_blueprint)
    from .api.user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    return app
