from . import db

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    icon_path = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)

db.create_all()