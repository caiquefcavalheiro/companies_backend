from flask import Flask
import dotenv
import os
from flask_sqlalchemy import SQLAlchemy

dotenv.load_dotenv()

db = SQLAlchemy()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = bool(
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    )
    db.init_app(app)
    app.db = db

    from app import models
