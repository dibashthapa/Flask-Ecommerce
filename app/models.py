from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseProduct(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    img_url = db.Column(db.String(255))
    category = db.Column(db.String(255))
    inventory = db.Column(db.Integer)
    price = db.Column(db.Integer)


class Fashion(BaseProduct):
    __tablename__ = "fashion"


class Jewelry(BaseProduct):
    __tablename__ = "jewelry"


class Bicycle(BaseProduct):
    __tablename__ = "bicycles"


class Apparel(BaseProduct):
    __tablename__ = "apparels"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(255))
    lname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
