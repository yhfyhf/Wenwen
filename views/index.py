from flask import render_template
from flask.ext.login import login_required
from mysite import app
from mysite.model.question import Question


@app.route('/')
@login_required
def index():
    return render_template('index.html',
        questions=Question.query.order_by(Question.id.desc()).all()
    )
