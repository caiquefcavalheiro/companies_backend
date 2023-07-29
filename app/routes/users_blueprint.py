from flask import Blueprint
from app.controllers.users_controller import UserController

bp = Blueprint("users", __name__, url_prefix="/users")

bp.get("")(UserController().list_users)
bp.post("")(UserController().create_user)
bp.patch("")
bp.delete("")
