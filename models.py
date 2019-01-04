from django.http import JsonResponse
from sys import exc_info
from traceback import format_exc


JSON_DUMPS = {"indent": 2, "sort_keys": False}


def result(data, status=200):
    response = {
        "type": "result",
        "data": data,
    }
    return JsonResponse(response, status=status, json_dumps_params=JSON_DUMPS)


def error(name, error_type=None, message=None, status=500):
    response = {
        "type": "error",
        "data": {
            "name": name,
            "type": error_type,
            "status_code": status,
            "message": message,
            "exception": get_exception(),
        },
    }
    return JsonResponse(response, status=status, json_dumps_params=JSON_DUMPS)


def method_not_allowed():
    return error("method-not-allowed", status=405)


def get_exception():
    type, value, traceback = exc_info()
    if type and value and traceback:
        return {
            "name": "{module}.{name}".format(module=type.__module__, name=type.__name__),
            "value": str(value),
            "stacktrace": format_exc().splitlines(),
        }
    else:
        return None
