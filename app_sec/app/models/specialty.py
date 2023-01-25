from app import db, login_manager
from flask_login import UserMixin

class Specialty(db.Model, UserMixin):
    __tablename__ = "specialties"
    id = db.Column("id", db.Integer, primary_key=True)

    name = db.Column("description", db.String(80), nullable=False, unique=True)
    description = db.Column("description", db.String(80), nullable=False)
    doctor = db.Column("Doctor", db.String(80), nullable=False)

    def is_active(self):
        return True

    def __init__(self, name, description, doctor):
        self.name = name
        self.description = description
        self.doctor = doctor

    def get_id(self):
        return self.id 