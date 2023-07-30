from flask import Flask
from .users_blueprint import bp as bp_users
from .login_blueprint import bp as bp_login
from .companies_blueprint import bp as bp_companies


def init_app(app: Flask):
    app.register_blueprint(bp_users)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_companies)
