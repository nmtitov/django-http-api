from .response import error


def handler400(request, exception):
    return error("client-error", status=400)


def handler403(request, exception):
    return error("permission denied", status=403)


def handler404(request, exception):
    return error("not-found", status=404)


def handler500(request):
    return error("internal-server-error", message="Some message hopefully explaining what's going on", status=500)
