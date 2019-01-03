from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_exempt
from .response import result, error, method_not_allowed


@csrf_exempt
def index(request):
    if request.method == "GET":
        data = {
           "message": "It works!",
        }
        return result(data)
    else:
        return method_not_allowed()


@csrf_exempt
def clients(request):
    if request.method == "GET":
        data = [
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
        ]
        return result(data)
    elif request.method == "POST":
        data = {
            "message": "Thanks for posting!",
        }
        return result(data, status=201)
    else:
        return method_not_allowed()


@csrf_exempt
def items(request):
    return method_not_allowed()


@csrf_exempt
def settings(request):
    return method_not_allowed()
