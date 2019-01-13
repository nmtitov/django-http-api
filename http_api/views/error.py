from ..utils.data_structures import error
from ..utils.decorators import json
from ..utils.exceptions import get_exception


# To enable custom error handlers add the following lines to the project urls.py file
# handler400 = 'http_api.views.error.handler400'
# handler403 = 'http_api.views.error.handler403'
# handler404 = 'http_api.views.error.handler404'
# handler500 = 'http_api.views.error.handler500'


@json
def handler400(request, exception):
    return error("client-error", error_type="handler400", exception=get_exception(), status=400)


@json
def handler403(request, exception):
    return error("permission-denied", error_type="handler403", exception=get_exception(), status=403)


@json
def handler404(request, exception):
    return error("not-found", error_type="handler404", exception=get_exception(), status=404)


@json
def handler500(request):
    return error("internal-server-error", error_type="handler500", exception=get_exception(), status=500)


@json
def csrf_failure(request, reason=""):
    return error("csrf-failure", error_type="csrf_failure", exception=get_exception(), status=403)
