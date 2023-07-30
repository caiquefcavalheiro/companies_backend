from flask import Blueprint
from app.controllers.companies_controller import CompaniesController

bp = Blueprint("companies", __name__, url_prefix="/companies")

bp.route("")(CompaniesController().list_companies)
bp.get("/<companie_id>")(CompaniesController().list_one_companie)
bp.post("")(CompaniesController().create_companie)
bp.patch("/<companie_id>")(CompaniesController().update_companie)
bp.delete("/<companie_cnpj>")(CompaniesController().delete_companie)
