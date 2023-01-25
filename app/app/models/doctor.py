from app import db, login_manager
from flask_login import UserMixin

class Doctor(db.Model, UserMixin):
    __tablename__ = "doctors"
    id = db.Column("id", db.Integer, primary_key=True)

    name = db.Column("name", db.String(80), nullable=False)
    email = db.Column("email", db.String(80), nullable=False)
    specialty = db.Column("specialty", db.String(80), nullable=False)
    phone_number = db.Column("phone_number", db.String(15), nullable=False)
    address = db.Column("address", db.String(80), nullable=False)
    ssn = db.Column("ssn", db.BigNumber, nullable=False)

    def is_active(self):
        return True

    def __init__(self, name, email, specialty, phone_number, address, ssn):
        self.name = name
        self.email = email
        self.specialty = specialty
        self.phone_number = phone_number
        self.address = address
        self.ssn = ssn


    def get_id(self):
        return self.id

 