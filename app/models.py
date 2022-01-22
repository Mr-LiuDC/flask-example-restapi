import datetime

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    """
    用户数据表
    """
    __tablename__ = 'sys_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    last_update_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    @staticmethod
    def create(username, raw_password, email):
        password_hash = generate_password_hash(raw_password)
        user = User(username=username, password_hash=password_hash, email=email)
        db.session.add(user)
        db.session.commit()
        return user

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, raw_password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(raw_password)

    def verify_password(self, raw_password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, raw_password)


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
