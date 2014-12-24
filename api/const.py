# encoding: utf-8

class Error(object):
    #### account 
    user_username_empty = "username empty"
    user_password_empty = "password empty"

    # login
    user_not_exist = "user not exist"
    user_wrong_password = "wrong password"

    # register 
    user_username_exist = "username exists"
    user_username_too_long = "username too long"
    user_password_too_long = "password too long"