from app.repository import InPostgresRepository
from flask import request
from http import HTTPStatus
from app.models import User
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity


class UserController:
    repository = InPostgresRepository()
    user_keys = ["name", "email", "password"]
    user_key_types = {"name": str, "email": str, "password": str}

    def list_users(self):
        return []

    def create_user(self):
        user_data = request.get_json()
        try:
            self.repository.create(user_data, User)
            return {"message": "create user sucessfull"}, HTTPStatus.CREATED
        except IntegrityError as e:
            return {"error": "Email already in use"}, HTTPStatus.CONFLICT

    @jwt_required()
    def update_user(self):
        user_id = get_jwt_identity()
        pass

    @jwt_required()
    def delete_user(self):
        user_id = get_jwt_identity()
        pass
