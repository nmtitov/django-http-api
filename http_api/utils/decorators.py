from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from ..utils.data_structures import error


def json_response(func):
    def decorator(request, *args, **kwargs):
        def get_status(response_body):
            try:
                return response_body.get("status_code")
            except AttributeError:
                return None
        response = func(request, *args, **kwargs)
        if response:
            status = get_status(response)
            return JsonResponse(response, safe=False, status=status, json_dumps_params={"indent": 2, "sort_keys": False})
        else:
            return HttpResponse("", status=204, content_type="application/json")
    return decorator


def authentication_required(func):
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
