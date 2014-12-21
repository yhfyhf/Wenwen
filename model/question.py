from datetime import datetime
from mysite import db

class Question(db.Model):

    __tablename__ = 'question'
    id = db.Column('question_id', db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    description = db.Column(db.String(10000))
    create_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.create_time = datetime.now()
        self.user_id = user_id
