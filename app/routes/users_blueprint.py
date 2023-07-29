from flask import Blueprint
from app.controllers.users_controller import UserController

bp = Blueprint("users", __name__, url_prefix="/users")

bp.get("")(UserController().list_users)
bp.get("/<user_id>")(UserController().list_one_user)
bp.post("")(UserController().create_user)
bp.patch("/<user_id>")(UserController().update_user)
bp.delete("/<user_id>")(UserController().delete_user)
