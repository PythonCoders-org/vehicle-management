from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

# DB classess
class Users(UserMixin, db.Model):

    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(100))
    username = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(100))
    user_role = db.Column(db.String(30))
    date = db.Column(db.DateTime)
    
    def __init__(self, userid=None, username=None, email=None, password=None, user_role=None, date=None):
        self.userid = userid
        self.username = username
        self.email = email
        self.password = password
        self.user_role = user_role
        self.date = date

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


# db.create_all()