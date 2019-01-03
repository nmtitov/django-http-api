from django.http import JsonResponse
from sys import exc_info
from traceback import format_exc


def result(data, status=200):
    response = {
        "type": "result",
        "data": data,
    }
    return JsonResponse(response, status=status, json_dumps_params={"indent": 2, "sort_keys": False})


def error(name, error_type=None, message=None, status=500):
    exc_type, value, traceback = exc_info()
    exception = {
        "exc_name": exc_type.__name__,
        "exc_type": str(exc_type),
        "value": str(value),
        "traceback": format_exc().splitlines(),
    }
    response = {
        "type": "error",
        "data": {
            "name": name,
            "error_type": error_type,
            "message": message,
            "exception": exception,
        },
    }
    return JsonResponse(response, status=status, json_dumps_params={"indent": 2, "sort_keys": False})


def method_not_allowed(message=None):
    return error("method-not-allowed", message=message, status=405)
