from flask import request, jsonify
from http import HTTPStatus
from app.models.user_model import User
from flask_jwt_extended import create_access_token
from datetime import timedelta


class LoginController:
    def login():
        login_data = request.get_json()

        found_user = User.query.filter_by(email=login_data["email"]).first()

        access_token = create_access_token(
            identity=found_user.id, expires_delta=timedelta(hours=1)
        )

        response = {"access_token": access_token}

        return jsonify(response), HTTPStatus.OK
