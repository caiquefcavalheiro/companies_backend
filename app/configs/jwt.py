import re
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from http import HTTPStatus


def init_app(app: Flask):
    jwt = JWTManager(app)

    @jwt.expired_token_loader
    def my_expired_token_callback(e, a):
        response = {"message": "The token has expired"}

        return jsonify(response), HTTPStatus.UNAUTHORIZED

    @jwt.unauthorized_loader
    def my_unauthorized_callback(e):
        response = {"message": "Unauthorized"}

        return jsonify(response), HTTPStatus.UNAUTHORIZED

    @jwt.invalid_token_loader
    def my_invalid_token_loader_callback(e):
        print(e)
        msg = "Invalid token."
        search = re.search("Bad", e)

        if search:
            msg = "Missing authorization token"

        response = jsonify({"message": msg})

        return response, HTTPStatus.UNAUTHORIZED
