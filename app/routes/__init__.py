from flask import Flask
from .users_blueprint import bp as bp_users
from .login_blueprint import bp as bp_login


def init_app(app: Flask):
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_login)
