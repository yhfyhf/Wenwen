from flask import render_template
from mysite import app
from mysite.model.question import Question


@app.route('/')
def index():
    return render_template('index.html',
        questions=Question.query.order_by(Question.id.desc()).all()
    )
