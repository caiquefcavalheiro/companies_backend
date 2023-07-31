from flask import request, jsonify
from http import HTTPStatus
from app.models.user_model import User
from flask_jwt_extended import create_access_token
from datetime import timedelta
import re


class LoginController:
    def login():
        login_data: dict = request.get_json()

        found_user: User = User.query.filter_by(email=login_data["email"]).first()

        if not found_user or not found_user.check_password(
            login_data.get("password", "")
        ):
            return {
                "message": "email or password are incorrect"
            }, HTTPStatus.BAD_REQUEST

        access_token = create_access_token(
            identity=found_user.id, expires_delta=timedelta(hours=1)
        )

        response = {"access_token": access_token}

        return jsonify(response), HTTPStatus.OK
