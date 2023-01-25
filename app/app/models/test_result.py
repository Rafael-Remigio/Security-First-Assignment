from app import db, login_manager
from flask_login import UserMixin 

class TestResult(db.Model, UserMixin):
    __tablename__ = "test_results"
 
    id = db.Column("id", db.Integer, primary_key=True)
    
    info = db.Column("info", db.String(80), nullable=False)
    doctor = db.Column("doctor", db.String(80), nullable=False)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"), nullable=False)


    def is_active(self):
        return True

    def __init__(self, info, doctor, user_id):

        self.info = info 
        self.doctor = doctor 
        self.user_id = user_id

    def get_code(self):
        return self.id
 