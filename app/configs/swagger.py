from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"


def init__app(app: Flask):
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "Companies"},
    )

    app.register_blueprint(swaggerui_blueprint)
