from sqlalchemy import Column, String, ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from uuid import uuid4
from app.exceptions import CNPJFormatError, CNAEFormatError
import re


@dataclass
class Companies(db.Model):
    __tablename__ = "companies"

    id: str
    cnae: str
    cnpj: str
    nome_fantasia: str
    nome_razao: str
    user_id: str

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    cnae = Column(String(7), nullable=False)
    cnpj = Column(String(18), nullable=False, unique=True)
    nome_fantasia = Column(String(255), nullable=False)
    nome_razao = Column(String(255), nullable=False)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    @validates("cnae")
    def verify_cnae(self, key, cnae_to_verify: str):
        regex = r"^\d{4}-\d{1}/\d{2}$"  # format 1111-2/33
        format_cnae = cnae_to_verify.replace("-", "").replace("/", "")

        if re.fullmatch(regex, cnae_to_verify):
            return format_cnae
        raise CNAEFormatError

    @validates("cnpj")
    def verify_cnpj(self, key, cnpj_to_verify: str):
        regex = r"^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$"  # format 11.222.333/4444-55
        format_cnpj = cnpj_to_verify.replace("/", "").replace(".", "").replace("-", "")

        if re.fullmatch(regex, cnpj_to_verify):
            return format_cnpj
        raise CNPJFormatError
