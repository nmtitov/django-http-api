from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "GET":
        data = {
            "type": "result",
            "data": {
                "message": "It works!",
            },
        }
        return JsonResponse(data, status=405)
    else:
        data = {
            "type": "error",
            "data": {
                "message": "Not allowed",
            },
        }
        return JsonResponse(data, status=405)


@csrf_exempt
def counterparties(request):
    if request.method == "GET":
        response = {
            "type": "result",
            "data": [
                {
                    "first_name": "Nikita",
                    "last_name": "Titov",
                    "email": "nmtitov@ya.ru",
                    "github": "https://github.com/nmtitov",
                },
                {
                    "first_name": "Nikita",
                    "last_name": "Titov",
                    "email": "nmtitov@ya.ru",
                    "github": "https://github.com/nmtitov",
                },
                {
                    "first_name": "Nikita",
                    "last_name": "Titov",
                    "email": "nmtitov@ya.ru",
                    "github": "https://github.com/nmtitov",
                },
            ],
        }
        return JsonResponse(response, status=200)
    elif request.method == "POST":
        data = {
            "type": "result",
            "data": {
                "message": "Hello, World!",
            },
        }
        return JsonResponse(data, status=200)
    else:
        data = {
            "type": "error",
            "data": {
                "message": "Not allowed",
            },
        }
        return JsonResponse(data, status=405)


@csrf_exempt
def items(request):
    data = {
        "type": "error",
        "data": {
            "message": "Not allowed",
        },
    }
    return JsonResponse(data, status=405)


@csrf_exempt
def settings(request):
    data = {
        "type": "error",
        "data": {
            "message": "Not allowed",
        },
    }
    return JsonResponse(data, status=405)
