from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(128))
    time = db.Column(db.DateTime(timezone=True), default=func.now())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    online = db.Column(db.Boolean, nullable=False, default=True)
