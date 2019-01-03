from django.http import JsonResponse


def handler400(request, exception):
    data = {
        "type": "error",
        "data": {
            "message": "Client error",
        },
    }
    return JsonResponse(data, status=400)


def handler403(request, exception):
    data = {
        "type": "error",
        "data": {
            "message": "Permission denied",
        },
    }
    return JsonResponse(data, status=403)


def handler404(request, exception):
    data = {
        "type": "error",
        "data": {
            "message": "Not found",
        },
    }
    return JsonResponse(data, status=404)


def handler500(request):
    data = {
        "type": "error",
        "data": {
            "message": "Internal server error",
        },
    }
    return JsonResponse(data, status=500)
