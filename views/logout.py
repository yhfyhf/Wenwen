from flask import url_for, redirect
from flask.ext.login import logout_user
from mysite import app

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
        