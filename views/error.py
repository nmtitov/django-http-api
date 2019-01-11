from ..data_structures import error
from ..helper import get_exception
from ..util import json_response


# To enable custom error handlers add the following lines to the project urls.py file
# handler400 = 'http_api.views.handler400'
# handler403 = 'http_api.views.handler403'
# handler404 = 'http_api.views.handler404'
# handler500 = 'http_api.views.handler500'


@json_response
def handler400(request, exception):
    return error("client-error", error_type="handler400", exception=get_exception(), status=400)


@json_response
def handler403(request, exception):
    return error("permission-denied", error_type="handler403", exception=get_exception(), status=403)


@json_response
def handler404(request, exception):
    return error("not-found", error_type="handler404", exception=get_exception(), status=404)


@json_response
def handler500(request):
    return error("internal-server-error", error_type="handler500", exception=get_exception(), status=500)


@json_response
def csrf_failure(request, reason=""):
    return error("csrf-failure", error_type="csrf_failure", exception=get_exception(), status=403)
