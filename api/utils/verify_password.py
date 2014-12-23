from flask import g
from mysite.api.token import auth
from mysite.model.user import User


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
    