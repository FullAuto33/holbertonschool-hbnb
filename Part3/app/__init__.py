# app/__init__.py

from flask import Flask
from config import DevelopmentConfig
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
jwt = JWTManager()
bcrypt = Bcrypt()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    bcrypt.init_app(app)
    jwt.init_app(app)

    return app
