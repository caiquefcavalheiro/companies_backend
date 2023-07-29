from flask import Flask
from .users_blueprint import bp as bp_users


def init_app(app: Flask):
    app.register_blueprint(bp_users)
