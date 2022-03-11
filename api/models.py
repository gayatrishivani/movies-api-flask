from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rating = db.Column(db.Integer)
    review = db.Column(db.String(200))

