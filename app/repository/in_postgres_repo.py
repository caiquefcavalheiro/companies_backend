from flask import request
from app.configs.database import db


class InPostgresRepository:
    def __init__(self) -> None:
        self.db = db
        self.session = self.db.session

    def list(self, Database: db.Model, sort, dir, start, limit):
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
        user = (
            self.session.query(Database)
            .select_from(Database)
            .filter(Database.id == id)
            .first()
        )

        return user

    def create(self, data, Database: db.Model):
        new_model = Database(**data)
        self.session.add(new_model)
        self.session.commit()

        return new_model

    def update(self, id: str, data, Database: db.Model):
        pass

    def delete(self, id: str, Database: db.Model):
        pass
