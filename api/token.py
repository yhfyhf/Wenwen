from flask import g, jsonify
from flask.ext.httpauth import HTTPBasicAuth
from mysite.model.user import User
from mysite.api import api, CONTENTTYPE


auth = HTTPBasicAuth()


@api.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'token': token.decode('ascii') }), 200, CONTENTTYPE

@auth.verify_password
def check_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.check_password(password):
            return False
    g.user = user
    return True
