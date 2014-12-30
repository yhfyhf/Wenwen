from mysite import db
from mysite.model import SerializableModel
from datetime import datetime
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class Answer(db.Model, SerializableModel):

    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer)
    content = db.Column(db.String(10000))
    create_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)

    def __init__(self, question_id, content, user_id):
        self.question_id = question_id
        self.content = content
        self.create_time = datetime.now()
        self.user_id = user_id

    def __repr__(self):
        return '<Answer %d to Question %d by user_id %d>' % (self.id, self.question_id, self.user_id)
