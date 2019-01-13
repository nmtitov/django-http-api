from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from functools import wraps
from ..utils.data_structures import error


def json(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        x = func(request, *args, **kwargs)
        if x is None:
            return _json_response(None, status=204)
        elif isinstance(x, dict) and "status_code" in x:
            status = x.get("status_code", None)
            body = x.get("body", None)
            return _json_response(body, status)
        else:
            return _json_response(x, None)
    return decorator


def _json_response(body, status):
    if body:
        return JsonResponse(body, safe=False, status=status, json_dumps_params={"indent": 2, "sort_keys": False})
    else:
        return HttpResponse("", status=status, content_type="application/json")


def auth(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        # If a user did login to the admin panel before and has a cookie, let him in (works only in browser)
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            token = request.META['HTTP_X_TOKEN']  # curl -i http://localhost:8000/api/ --header "X-Token: 000"
            user = authenticate(request, token=token)
            if user is not None:
                login(request, user)
                return func(request, *args, **kwargs)
            else:
                return error("Authentication required", error_type="authentication", status=403)
    return decorator
