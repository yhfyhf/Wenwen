# encoding: utf-8
from werkzeug.security import generate_password_hash, check_password_hash
from mysite import db
from datetime import datetime


class User(db.Model):

    __tablename__ = "user"
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True)
    password = db.Column('password', db.String(250))
    email = db.Column('email', db.String(50), unique=True)
    reg_time = db.Column('reg_time', db.DateTime)
    description = db.Column('description', db.String(200))
    n_uped = db.Column('n_uped', db.Integer)
    n_downed = db.Column('n_downed', db.Integer)


    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email
        self.reg_time = datetime.now()
        self.description =""
        self.n_uped = self.n_downed = 0

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password , password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
