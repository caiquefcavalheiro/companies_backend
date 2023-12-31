from flask import Flask
from app.configs import database, migration, env_configs, jwt, swagger
from app import routes


def create_app():
    app = Flask(__name__)

    env_configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    routes.init_app(app)
    jwt.init_app(app)
    swagger.init__app(app)

    return app
