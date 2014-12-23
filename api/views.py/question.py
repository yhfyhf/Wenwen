from flask import jsonify
from mysite.model.question import Question
from mysite.api import api, CONTENTTYPE
from mysite.api.token import auth


@api.route('/questions', methods=['GET'])
@auth.login_required
def questions():
    questions = Question.query.order_by('-id').limit(5).all()
    ret = jsonify({ "questions": [q.to_dict() for q in questions] })
    return ret, 200, CONTENTTYPE
