from flask import jsonify


def ok(content=""):
    message = {
        "status" : "OK",
        "content": content,
    }
    return jsonify(message)

def error(error=""):
    if isinstance(error, (tuple, list)):
        message = {
            'status' : 'error',
            'code'   : error[0],
            'message': error[1],
        }
    else:
        message = {
            'status' : 'error',
            'message': error,
        }

    return jsonify(message)
    