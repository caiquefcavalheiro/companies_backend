from app.models.user_model import User
import dotenv
import os
from app.exceptions import PermissionError
import re

dotenv.load_dotenv()


class PermissionsService:
    def check_if_user_owner_or_admin(self, user_id, looged_id):
        get_user_logged = User.query.filter_by(id=looged_id).first()

        admin_email = os.environ.get("ADMIN_EMAIL")

        if re.fullmatch(admin_email, get_user_logged.email) or looged_id == user_id:
            return
        raise PermissionError
