from app import db, login_manager
from flask_login import UserMixin

class AppRequest(db.Model, UserMixin):
    __tablename__ = "app_requets"
    id = db.Column("id", db.Integer, primary_key=True)

    description = db.Column("description", db.String(80), nullable=False)
    specialty_id = db.Column("specialty_id", db.String(80), nullable=False)

    def is_active(self):
        return True

    def __init__(self, description, specialty_id):
        self.description = description
        self.specialty_id = specialty_id

    def get_id(self):
        return self.id

 