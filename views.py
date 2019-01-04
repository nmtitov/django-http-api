from django.http import JsonResponse
from .models import error


def json_response(func):
    def decorator(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        status = response["status_code"]
        return JsonResponse(response, status=status, json_dumps_params={"indent": 2, "sort_keys": False})
    return decorator


# To enable handlers add the following lines to the project urls.py file
# handler400 = 'http_api.views.handler400'
# handler403 = 'http_api.views.handler403'
# handler404 = 'http_api.views.handler404'
# handler500 = 'http_api.views.handler500'


@json_response
def handler400(request, exception):
    return error("client-error", error_type="handler400", status=400)


@json_response
def handler403(request, exception):
    return error("permission denied", error_type="handler403", status=403)


@json_response
def handler404(request, exception):
    return error("not-found", error_type="handler404", status=404)


@json_response
def handler500(request):
    return error("internal-server-error", error_type="handler500", status=500)

