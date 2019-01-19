from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_safe

from http_api.utils.data_structures import error, result
from http_api.utils.decorators import require_auth, json


@csrf_exempt
@require_safe
@json
def index(request):
    return result({
        "message": "It works!",
    })


@csrf_exempt
@require_safe
@json
@require_auth
def user(request):
    obj = request.user
    # Prepare response
    email = obj.email if obj.email else None
    data = {
        "email": email,
    }
    return result(data)


@csrf_exempt
@require_safe
@json
def sample_error(request):
    return error("sample-error", error_type="sample_error", message="This is an example of erroneous response with a custom status code", status=520)


@csrf_exempt
@require_safe
@json
def sample_exception(request):
    raise SuspiciousOperation("sample_exception")


@csrf_exempt
@require_http_methods(["GET", "HEAD", "POST"])
@json
def clients(request):
    if request.method == "GET" or request.method == "HEAD":
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
        }
        return result(data, status=201)
    else:
        return None


@csrf_exempt
@require_safe
@json
@require_auth
def secret(request):
    return result({"message": "This is my secret"})


# Empty response
@csrf_exempt
@json
def empty(request):
    return None


# Empty response with a custom status code
@csrf_exempt
@json
def empty_status(request):
    return {
        "status_code": 404,
        "body": None,
    }


# List response
@csrf_exempt
@require_safe
@json
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
@require_safe
@json
def united_states(request):
    return {
        "country": "United States",
        "capital": "Washington, D.C.",
        "largest_city": "New York City",
        "national_language": "English",
        "area": "9833520",
    }
