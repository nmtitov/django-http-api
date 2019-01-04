from sys import exc_info
from traceback import format_exc


def result(data, status=200):
    return {
        "type": "result",
        "status_code": status,
        "data": data,
    }


def error(name, error_type=None, message=None, status=520):
    return {
        "type": "error",
        "status_code": status,
        "data": {
            "name": name,
            "type": error_type,
            "message": message,
            "exception": get_exception(),
        },
    }


def method_not_allowed():
    return error("method-not-allowed", status=405)


def get_exception():
    exc_type, value, traceback = exc_info()
    if exc_type and value and traceback:
        return {
            "name": "{module}.{name}".format(module=type.__module__, name=type.__name__),
            "value": str(value),
            "stacktrace": format_exc().splitlines(),
        }
    else:
        return None
