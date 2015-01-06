#encoding: utf-8
from flask import render_template, request, g, redirect, url_for, flash
from flask.ext.login import login_required
from mysite import app, db
from mysite.model.question import Question
from mysite.model.answer import Answer
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


@app.route('/answer/add/<int:question_id>', methods=['POST'])
@login_required
def answer(question_id):
    answer_content = request.form['content'].strip()
    if not answer_content:
        flash(u'Please write down your answer!', 'error')
    if not Question.query.get(question_id):
        return redirect(url_for('index'))
    else:
        answer = Answer(question_id, answer_content, g.user.id)
        db.session.add(answer)
        db.session.commit()
        flash(u'Add your answer successfully!')
    return redirect(url_for('show_or_update', question_id=question_id))
