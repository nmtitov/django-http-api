from django.http import JsonResponse


def error(name, message=None, status=500):
    data = {
        "type": "error",
        "data": {
            "name": name,
            "message": message,
        },
    }
    return JsonResponse(data, status=status)
