from app.repository import InPostgresRepository
from flask import request, jsonify
from http import HTTPStatus
from app.models import User
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions import (
    InvalidIdError,
    InvalidPaginateParams,
    AttributeTypeError,
    MissingKeysError,
)
from app.services.general_services import GeneralServices
from app.services.paginate_list_services import PaginateListServices


class UserController:
    repository = InPostgresRepository()
    user_keys = ["name", "email", "password"]
    user_key_types = {"name": str, "email": str, "password": str}

    def list_users(self):
        start = int(request.args.get("start", 0))
        limit = int(request.args.get("limit", 10))
        sort = request.args.get("sort", "id")
        dir = request.args.get("dir", "asc")

        try:
            PaginateListServices().validate_page_atributes(
                start, limit, sort, dir, ["name", "email", "id"]
            )
        except InvalidPaginateParams as e:
            return jsonify(e.response), e.status_code

        users_list = self.repository.list(User, sort, dir, start, limit)

        return jsonify(users_list), HTTPStatus.OK

    def list_one_user(self, user_id):
        try:
            GeneralServices().validate_id(user_id, User)

            find_user = self.repository.list_one(user_id, User)

        except InvalidIdError as e:
            return jsonify(e.response), e.status_code

        return jsonify(find_user), HTTPStatus.OK

    def create_user(self):
        user_data = request.get_json()
        try:
            check_data = GeneralServices().check_keys(user_data, self.user_keys)
            GeneralServices().check_keys_type(check_data, self.user_key_types)

            self.repository.create(check_data, User)
            return {"message": "create user sucessfull"}, HTTPStatus.CREATED
        except IntegrityError:
            return {"error": "Email already in use"}, HTTPStatus.CONFLICT
        except (AttributeTypeError, MissingKeysError) as e:
            return e.response, e.status_code

    @jwt_required()
    def update_user(self, user_id):
        logged_user_id = get_jwt_identity()
        update_data = request.get_json()

        try:
            GeneralServices().validate_id(user_id, User)

            check_data, _ = GeneralServices().remove_unnecessary_keys(
                update_data, self.user_keys
            )

            GeneralServices().check_keys_type(check_data, self.user_key_types)

            update_user = self.repository.update(user_id, check_data, User)

            return jsonify(update_user), HTTPStatus.OK

        except IntegrityError:
            return {"error": "Email already in use"}, HTTPStatus.CONFLICT
        except (AttributeTypeError, MissingKeysError, InvalidIdError) as e:
            return e.response, e.status_code

    @jwt_required()
    def delete_user(self, user_id: str):
        user_id = get_jwt_identity()

        pass
