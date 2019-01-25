from ..utils.data_structures import error
from ..utils.exceptions import get_exception_info
from ..views.decorators.api import jsonify

# To enable custom error handlers add the following lines to the project urls.py file
# handler400 = 'http_api.views.error.handler400'
# handler403 = 'http_api.views.error.handler403'
# handler404 = 'http_api.views.error.handler404'
# handler500 = 'http_api.views.error.handler500'


@jsonify
def handler400(request, exception):
    return error("client-error", error_type="handler400", exception_info=get_exception_info(), status=400)


@jsonify
def handler403(request, exception):
    return error("permission-denied", error_type="handler403", exception_info=get_exception_info(), status=403)


@jsonify
def handler404(request, exception):
    return error("not-found", error_type="handler404", exception_info=get_exception_info(), status=404)


@jsonify
def handler500(request):
    return error("internal-server-error", error_type="handler500", exception_info=get_exception_info(), status=500)


@jsonify
def csrf_failure(request, reason=""):
    return error("csrf-failure", error_type="csrf_failure", exception_info=get_exception_info(), status=403)
