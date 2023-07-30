from app.repository import InPostgresRepository
from flask import request, jsonify
from http import HTTPStatus
from app.models import Companies
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.exceptions import (
    InvalidIdError,
    InvalidPaginateParamsError,
    AttributeTypeError,
    MissingKeysError,
    PermissionError,
    CNPJFormatError,
    CNAEFormatError,
    CNPJNotFound,
)
from app.services.general_services import GeneralServices
from app.services.paginate_list_services import PaginateListServices
from app.services.permissions_services import PermissionsService


class CompaniesController:
    repository = InPostgresRepository()
    companie_keys = ["cnae", "cnpj", "nome_fantasia", "nome_razao"]
    companie_key_types = {
        "cnae": str,
        "cnpj": str,
        "nome_fantasia": str,
        "nome_razao": str,
    }

    def list_companies(self):
        try:
            start = int(request.args.get("start", 0))
            limit = int(request.args.get("limit", 10))
            sort = request.args.get("sort", "id")
            dir = request.args.get("dir", "asc")

            PaginateListServices().validate_page_atributes(
                start,
                limit,
                sort,
                dir,
                ["id", "cnae", "cnpj", "nome_fantasia", "nome_razao"],
            )
        except InvalidPaginateParamsError as e:
            return jsonify(e.response), e.status_code
        except ValueError:
            return (
                jsonify({"message": "limit and start need to be number"}),
                HTTPStatus.BAD_REQUEST,
            )

        companies_list = self.repository.list(Companies, sort, dir, start, limit)

        return jsonify(companies_list), HTTPStatus.OK

    def list_one_companie(self, companie_id: str):
        try:
            GeneralServices().validate_id(companie_id, Companies)
            find_companie = self.repository.list_one(companie_id, Companies)

        except InvalidIdError as e:
            return jsonify(e.response), e.status_code

        return jsonify(find_companie), HTTPStatus.OK

    @jwt_required()
    def create_companie(self):
        companie_data = request.get_json()
        logged_user_id = get_jwt_identity()

        try:
            check_data = GeneralServices().check_keys(companie_data, self.companie_keys)
            GeneralServices().check_keys_type(check_data, self.companie_key_types)

            self.repository.create_with_relation(
                check_data, Companies, logged_user_id, "user_id"
            )
            return {"message": "create companie sucessfull"}, HTTPStatus.CREATED
        except IntegrityError:
            return {"message": "CNPJ is already registered"}, HTTPStatus.BAD_REQUEST
        except (
            AttributeTypeError,
            MissingKeysError,
            CNAEFormatError,
            CNPJFormatError,
        ) as e:
            return e.response, e.status_code

    @jwt_required()
    def update_companie(self, companie_id: str):
        logged_user_id = get_jwt_identity()
        update_data = request.get_json()

        try:
            GeneralServices().validate_id(companie_id, Companies)

            PermissionsService().check_if_user_is_companie_owner_or_admin(
                companie_id, logged_user_id
            )

            check_data, _ = GeneralServices().remove_unnecessary_keys(
                update_data, ["cnae", "nome_fantasia"]
            )

            GeneralServices().check_keys_type(check_data, self.companie_key_types)

            update_user = self.repository.update(companie_id, check_data, Companies)

            return jsonify(update_user), HTTPStatus.OK

        except IntegrityError:
            return {"message": "Email already in use"}, HTTPStatus.CONFLICT
        except (
            AttributeTypeError,
            MissingKeysError,
            InvalidIdError,
            PermissionError,
            CNPJNotFound,
            CNAEFormatError,
        ) as e:
            return e.response, e.status_code

    @jwt_required()
    def delete_companie(self, companie_cnpj: str):
        logged_user_id = get_jwt_identity()

        try:
            GeneralServices().validate_cnpj(companie_cnpj, Companies)
            PermissionsService().check_if_user_is_companie_owner_or_admin(
                companie_cnpj, logged_user_id, "cnpj"
            )
            self.repository.delete(companie_cnpj, Companies, "cnpj")
        except (
            InvalidIdError,
            PermissionError,
            CNPJNotFound,
        ) as e:
            return e.response, e.status_code

        return "", HTTPStatus.NO_CONTENT
