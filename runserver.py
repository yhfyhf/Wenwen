#!/usr/bin/env python
from flask import g
from flask.ext.login import LoginManager, current_user
from mysite import app, db
from mysite.model.user import User



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user


if __name__ == '__main__':
    db.create_all()
    app.run()
