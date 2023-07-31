from flask import request
from app.configs.database import db


class InPostgresRepository:
    def __init__(self) -> None:
        self.db = db
        self.session = self.db.session

    def list(self, Database: db.Model, sort: str, dir: str, start: int, limit: int):
        list_data = (
            self.session.query(Database)
            .order_by(getattr(getattr(Database, sort), dir)())
            .offset(start)
            .limit(limit)
        ).all()

        return {
            "start": start,
            "limit": limit,
            "sort": sort,
            "dir": dir,
            "data": list_data,
        }

    def list_one(self, id: str, Database: db.Model):
        model = self.session.query(Database).filter(Database.id == id).first()

        return model

    def create(self, data: dict, Database: db.Model):
        new_model = Database(**data)
        self.session.add(new_model)
        self.session.commit()

        return new_model

    def create_with_relation(
        self, data: dict, Database: db.Model, id: str, relation_field_name: str
    ):
        new_model = Database(**data)

        setattr(new_model, relation_field_name, id)
        self.session.add(new_model)
        self.session.commit()

        return new_model

    def update(self, id: str, data: dict, Database: db.Model):
        updade_model = self.session.query(Database).filter(Database.id == id).first()

        for key, value in data.items():
            setattr(updade_model, key, value)

        self.session.commit()

        return updade_model

    def delete(self, id: str, Database: db.Model, field: str = "id"):
        user_to_delete = (
            self.session.query(Database).filter(getattr(Database, field) == id).first()
        )

        self.session.delete(user_to_delete)
        self.session.commit()
