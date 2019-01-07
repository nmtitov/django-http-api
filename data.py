def result(data, status=200):
    return {
        "type": "result",
        "status_code": status,
        "data": data,
    }


def error(name, error_type=None, message=None, exception=None, status=520):
    return {
        "type": "error",
        "status_code": status,
        "data": {
            "name": name,
            "type": error_type,
            "message": message,
            "exception": exception,
        },
    }


def error_method_not_allowed():
    return error("method-not-allowed", status=405)
