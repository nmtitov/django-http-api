from .response import error


def handler400(request, exception):
    return error("client-error", error_type="handler400", status=400)


def handler403(request, exception):
    return error("permission denied", error_type="handler403", status=403)


def handler404(request, exception):
    return error("not-found", error_type="handler404", status=404)


def handler500(request):
    return error("internal-server-error", error_type="handler500", status=500)
