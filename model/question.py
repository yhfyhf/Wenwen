from datetime import datetime
from mysite import db
from mysite.model import SerializableModel
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class Question(db.Model, SerializableModel):

    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    description = db.Column(db.String(10000))
    create_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.create_time = datetime.now()
        self.user_id = user_id

    def __repr__(self):
        return '<Question %d by user_id %d>' % (self.id, self.user_id)
