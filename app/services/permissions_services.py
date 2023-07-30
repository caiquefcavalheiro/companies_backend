from app.models import User, Companies
import dotenv
import os
from app.exceptions import PermissionError
import re

dotenv.load_dotenv()


class PermissionsService:
    def check_if_user_owner_or_admin(self, user_id: str, logged_id: str):
        get_user_logged = User.query.filter_by(id=logged_id).first()

        admin_email = os.environ.get("ADMIN_EMAIL")

        if re.fullmatch(admin_email, get_user_logged.email) or logged_id == user_id:
            return
        raise PermissionError

    def check_if_user_is_companie_owner_or_admin(
        self, field_value: str, logged_id: str, field_name: str = "id"
    ):
        get_user_logged = User.query.filter_by(id=logged_id).first()

        filter_by = {}

        filter_by[field_name] = field_value

        get_companie = Companies.query.filter_by(**filter_by).first()

        admin_email = os.environ.get("ADMIN_EMAIL")

        if re.fullmatch(admin_email, get_user_logged.email) or re.fullmatch(
            logged_id, str(get_companie.user_id)
        ):
            return
        raise PermissionError
