from enum import unique
from re import T
from flask_sqlalchemy import SQLAlchemy




db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    