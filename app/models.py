from . import db

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime(), nullable=False)    
    project_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    tags = db.Column(db.String(255), nullable=False)
    tools = db.Column(db.String(255), nullable=False)
    project_link = db.Column(db.String(255), nullable=False)
    thumbnail_link = db.Column(db.String(255), nullable=True, default="")
    icon_link = db.Column(db.String(255), nullable=True, default="")

db.create_all()