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
    response = {
        "type": "error",
        "data": {
            "name": name,
            "type": error_type,
            "message": message,
            "exception": get_exception(),
        },
    }
    return JsonResponse(response, status=status, json_dumps_params={"indent": 2, "sort_keys": False})


def method_not_allowed(message=None):
    return error("method-not-allowed", message=message, status=405)


def get_exception():
    type, value, traceback = exc_info()
    if type and value and traceback:
        return {
            "name": "{module}.{name}".format(module=type.__module__, name=type.__name__),
            "value": str(value),
            "traceback": format_exc().splitlines(),
        }
    else:
        return None
