from django.http import JsonResponse


def result(data, status=200):
    response = {
        "type": "result",
        "data": data,
    }
    return JsonResponse(response, status=status)


def error(name, message=None, status=500):
    response = {
        "type": "error",
        "data": {
            "name": name,
            "message": message,
        },
    }
    return JsonResponse(response, status=status)


def method_not_allowed(message=None):
    return error("method-not-allowed", message=message, status=405)
