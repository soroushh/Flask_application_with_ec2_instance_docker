from flask_app import db

class Person(db.Model):
    """The definition of person class"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    family = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
