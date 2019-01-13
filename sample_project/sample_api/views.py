from django.views.decorators.csrf import csrf_exempt
from http_api.utils.data_structures import error, error_method_not_allowed, result
from http_api.utils.decorators import authentication_required, json_response


@csrf_exempt
@json_response
def index(request):
    if request.method == "GET":
        data = {
            "message": "It works!",
        }
        return result(data)
    else:
        return error_method_not_allowed()


@csrf_exempt
@json_response
@authentication_required
def user(request):
    if request.method == "GET":
        obj = request.user
        # Prepare response
        data = {
            "email": obj.email,
        }
        return result(data)
    else:
        return error_method_not_allowed()


@csrf_exempt
@json_response
def clients(request):
    if request.method == "GET":
        data = [
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
                   "first_name": "Nikita",
                   "last_name": "Titov",
                   "email": "nmtitov@ya.ru",
                   "github": "https://github.com/nmtitov",
               },
        return result(data, status=201)
    else:
        return error_method_not_allowed()


@csrf_exempt
@json_response
@authentication_required
def secret(request):
    if request.method == "GET":
        return result({"message": "This is my secret"})
    else:
        return error_method_not_allowed()
