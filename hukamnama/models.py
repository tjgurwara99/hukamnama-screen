# models.py

from flask_login import UserMixin
from datetime import datetime, timezone
from . import db


class User(UserMixin, db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class CurrentHukamnama(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    date = db.Column(db.Date, default=datetime.today)
    shabad_id = db.Column(db.String(100))
