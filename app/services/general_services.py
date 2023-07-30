from app.configs.database import db
from app.exceptions import (
    InvalidIdError,
    AttributeTypeError,
    MissingKeysError,
    CNPJNotFound,
)
import uuid


class GeneralServices:
    def validate_id(self, id: str, Model: db.Model):
        try:
            uuid.UUID(id)
        except ValueError:
            raise InvalidIdError

        search_info = Model.query.filter_by(id=id).first()

        if not search_info:
            raise InvalidIdError({"message": f"The id {id} not found"}, 404)

    def validate_cnpj(self, cnpj: str, Model: db.Model):
        search_info = Model.query.filter_by(cnpj=cnpj).first()

        if not search_info:
            raise CNPJNotFound(cnpj)

    def remove_unnecessary_keys(self, data: dict, necessary_keys: list):
        new_data = data.copy()
        not_used_keys = necessary_keys.copy()

        for key in data.keys():
            if key in necessary_keys:
                not_used_keys.remove(key)
            else:
                new_data.pop(key)

        return (new_data, not_used_keys)

    def check_keys(self, data: dict, mandatory_keys: list):
        new_data, missing_keys = self.remove_unnecessary_keys(data, mandatory_keys)

        if missing_keys:
            raise MissingKeysError(missing_keys)

        return new_data

    def check_keys_type(self, data: dict, keys_type: dict):
        for key, value in data.items():
            if type(value) is not keys_type[key]:
                raise AttributeTypeError(value, keys_type[key])
