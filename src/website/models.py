from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    files = db.relationship('File', backref='user', passive_deletes=True)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String)
    date_uploaded = db.Column(db.DateTime(timezone=True), default=func.now())
    uploader = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)