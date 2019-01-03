from django.http import JsonResponse


def index(request):
    data = {
        "type": "result",
        "data": {
            "reply": "It works!",
        },
    }
    return JsonResponse(data, status=405)


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
                "reply": "Hello, World!",
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


def items(request):
    data = {
        "type": "error",
        "data": {
            "message": "Not allowed",
        },
    }
    return JsonResponse(data, status=405)


def settings(request):
    data = {
        "type": "error",
        "data": {
            "message": "Not allowed",
        },
    }
    return JsonResponse(data, status=405)
