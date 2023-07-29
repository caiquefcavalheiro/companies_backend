from app.configs.database import db
from app.exceptions import InvalidIdError


class GeneralServices:
    def validate_id(self, id: str, Model: db.Model):
        if len(id) != 36:
            raise InvalidIdError

        search_info = Model.query.filter_by(id=id).first()

        if not search_info:
            raise InvalidIdError({"message": f"The id {id} not found"})
