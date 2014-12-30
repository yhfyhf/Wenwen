# encoding: utf-8
from flask import render_template, request, g, redirect, url_for, flash
from flask.ext.login import login_required
from mysite import app, db
from mysite.model.question import Question
from mysite.model.answer import Answer 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


@app.route('/questions/<int:question_id>', methods = ['GET' , 'POST'])
@login_required
def show_or_update(question_id):
    question = Question.query.get(question_id)
    if request.method == 'GET':
        return render_template('view.html', question=question)
    if question.user_id == g.user.id:
        question.title = request.form['title']
        question.description  = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    flash(u'只有原作者才有修改问题的权限!','error')
    return redirect(url_for('show_or_update', question_id=question.id))
