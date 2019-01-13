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
        data = [{
            "first_name": "Nikita",
            "last_name": "Titov",
            "email": "nmtitov@ya.ru",
            "github": "https://github.com/nmtitov",
        }, {
            "first_name": "Nikita",
            "last_name": "Titov",
            "email": "nmtitov@ya.ru",
            "github": "https://github.com/nmtitov",
        }, {
            "first_name": "Nikita",
            "last_name": "Titov",
            "email": "nmtitov@ya.ru",
            "github": "https://github.com/nmtitov",
        }]
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


# Empty response
@csrf_exempt
@json_response
def empty(request):
    return None


# Empty response with a custom status code
@csrf_exempt
@json_response
def empty_status(request):
    return {
        "status_code": 404,
        "body": None,
    }


# List response
@csrf_exempt
@json_response
def greetings(request):
    return [{
        "language": "English",
        "greeting": "Hello",
    }, {
        "language": "French",
        "greeting": "Bonjour",
    }, {
        "language": "Spanish",
        "greeting": "Hola",
    }, {
        "language": "German",
        "greeting": "Hallo",
    }, {
        "language": "Italian",
        "greeting": "Ciao",
    }, {
        "language": "Portugese",
        "greeting": "Ola",
    }]


# A plain dict response with a custom structure (keep in mind that "status_code" and "body" keys are reserved)
@csrf_exempt
@json_response
def united_states(request):
    return {
        "country": "United States",
        "capital": "Washington, D.C.",
        "largest_city": "New York City",
        "national_language": "English",
        "area": "9833520",
    }
