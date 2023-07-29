import os
import dotenv
from flask import Flask


dotenv.load_dotenv()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = bool(
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    )
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
