from app import db, login_manager
from flask_login import UserMixin

class ContactMessage(db.Model, UserMixin):
    __tablename__ = "contactMessage"

    id = db.Column("id", db.Integer, primary_key=True)

    textMessage = db.Column("textMessage", db.String(500), nullable=False,unique=False)
    name = db.Column("name", db.String(80), nullable=False, unique=False)
    email = db.Column("email", db.String(80), nullable=False,unique=False)

    def is_active(self):
        return True

    def __init__(self, textMessage, name,email):
        self.textMessage = textMessage
        self.name = name
        self.email = email

    def get_id(self):
        return self.id

