from app import db, login_manager
from flask_login import UserMixin

class Review(db.Model, UserMixin):
    __tablename__ = "reviews"

    id = db.Column("id", db.Integer, primary_key=True)

    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"), nullable=False)
    message = db.Column("message_", db.String(20), nullable=False)
    rating = db.Column("rating", db.String(80), nullable=False)


    def is_active(self):
        return True

    def __init__(self, message, rating, user_id):
        self.message = message
        self.rating = rating
        self.user_id = user_id

    def get_id(self):
        return self.id 
