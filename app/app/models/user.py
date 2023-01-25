from app import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(20), nullable=False, unique=True)
    password = db.Column("password", db.String(80), nullable=False)

    def is_active(self):
        return True

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()
