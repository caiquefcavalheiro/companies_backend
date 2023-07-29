from flask import request
from app.configs.database import db


class InPostgresRepository:
    def __init__(self) -> None:
        self.db = db
        self.session = self.db.session
        pass

    def create(self, data, Database):
        new_model = Database(**data)
        self.session.add(new_model)
        self.session.commit()

        return new_model
