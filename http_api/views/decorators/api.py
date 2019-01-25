from functools import wraps
from json import dumps
from operator import methodcaller

from django.contrib.auth import authenticate, login
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponse

from http_api.utils.data_structures import error, result


def jsonify(func):
    def _json_response(body, status):
        response_body = "" if not body else dumps(body, ensure_ascii=False, indent=2, sort_keys=False)
        return HttpResponse(response_body, status=status, content_type="application/json")

    @wraps(func)
    def decorator(request, *args, **kwargs):
        view_result = func(request, *args, **kwargs)
        if view_result is None:
            return _json_response(None, status=204)
        # if view_result is {"status_code": Any, "body": Any}
        elif isinstance(view_result, dict) and "status_code" in view_result and "body" in view_result:
            status = view_result.get("status_code", None)
            body = view_result.get("body", None)
            return _json_response(body, status)
        else:
            return _json_response(view_result, None)
    return decorator


def require_auth(func):
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


def pagify(per_page=10):
    def decorator(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            seq = func(request, *args, **kwargs)
            try:
                current_page = request.GET.get('page', 1)
                paginator = Paginator(seq, per_page=per_page)
                objects = paginator.get_page(current_page)
                page = paginator.page(current_page)
                return result({
                    "pager": {
                        "total": paginator.num_pages,
                        "next": page.next_page_number() if page.has_next() else None,
                        "previous": page.previous_page_number() if page.has_previous() else None,
                    },
                    "items": list(map(methodcaller('__dump__'), objects)) if all(hasattr(obj, '__dump__') for obj in objects) else objects
                })
            except EmptyPage:
                return error("empty-page", error_type="pager", message="The requested page is empty", exception_info=None, status=404)
        return _decorator
    return decorator
