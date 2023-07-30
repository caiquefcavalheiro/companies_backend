from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"


def init__app(app: Flask):
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "Test application"},
        oauth_config={
            "clientId": "your-client-id",
            "clientSecret": "your-client-secret-if-required",
            "realm": "your-realms",
            "appName": "your-app-name",
            "scopeSeparator": " ",
            "additionalQueryStringParams": {"test": "hello"},
        },
    )

    app.register_blueprint(swaggerui_blueprint)
