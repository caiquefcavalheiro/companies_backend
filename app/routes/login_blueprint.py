from flask import Blueprint

from app.controllers.login_controller import LoginController

bp = Blueprint("login", __name__, url_prefix="/login")

bp.post("")(LoginController.login)
