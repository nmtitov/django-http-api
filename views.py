from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from sys import exc_info
from traceback import format_exc
from .data import error


def json_response(func):
    def decorator(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        status = response.get("status_code")
        return JsonResponse(response, status=status, json_dumps_params={"indent": 2, "sort_keys": False})
    return decorator


# To enable handlers add the following lines to the project urls.py file
# handler400 = 'http_api.views.handler400'
# handler403 = 'http_api.views.handler403'
# handler404 = 'http_api.views.handler404'
# handler500 = 'http_api.views.handler500'


def get_exception():
    exc_type, value, traceback = exc_info()
    if exc_type and value and traceback:
        return {
            "name": "{module}.{name}".format(module=exc_type.__module__, name=exc_type.__name__),
            "value": str(value),
            "stacktrace": format_exc().splitlines(),
        }
    else:
        return None


@json_response
def handler400(request, exception):
    return error("client-error", error_type="handler400", exception=get_exception(), status=400)


@json_response
def handler403(request, exception):
    return error("permission denied", error_type="handler403", exception=get_exception(), status=403)


@json_response
def handler404(request, exception):
    return error("not-found", error_type="handler404", exception=get_exception(), status=404)


@json_response
def handler500(request):
    return error("internal-server-error", error_type="handler500", exception=get_exception(), status=500)


def authentication_required(func):
    def decorator(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        token = request.META['HTTP_X_TOKEN']
        user = authenticate(request, token=token)
        if user is not None:
            login(request, user)
            return func(request, *args, **kwargs)
        else:
            return error("Authentication required", error_type="authentication", status=403)
    return decorator
