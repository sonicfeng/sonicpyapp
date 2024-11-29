from sqlalchemy_serializer import SerializerMixin

from sonicpyapp.ext.database import db


class Product(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric())
    description = db.Column(db.Text)


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))


"Sonic test for DB usage, to store a dummy field value"
class Rotation(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    person = db.Column(db.String(140))
    day = db.Column(db.String(140))
