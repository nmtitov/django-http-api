from functools import wraps
from json import dumps

from django.contrib.auth import authenticate, login
from django.core.paginator import EmptyPage, Paginator
from django.http import HttpResponse

from http_api.utils.data_structures import error, result
from django.core.exceptions import PermissionDenied


def jsonify(func):
    def json_response(body, status):
        response_body = dumps(body, ensure_ascii=False, indent=2, sort_keys=False) if body else ""
        return HttpResponse(response_body, status=status, content_type="application/json")

    @wraps(func)
    def decorator(request, *args, **kwargs):
        view = func(request, *args, **kwargs)
        if view is None:
            return json_response(None, status=204)
        # if view_result is {"status_code": Any, "body": Any}
        elif isinstance(view, dict) and "status_code" in view and "body" in view:
            status = view["status_code"]
            body = view["body"]
            return json_response(body, status)
        else:
            return json_response(view, None)
    return decorator


def require_auth(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        # If a user did login to the admin panel before and has a cookie, let him in (useful in browser)
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            token = request.META['HTTP_X_TOKEN']  # curl -i http://localhost:8000/api/ --header "X-Token: 000"
            user = authenticate(request, token=token)
            if user:
                login(request, user)
                return func(request, *args, **kwargs)
            else:
                raise PermissionDenied()
    return decorator


def pager(per_page=10):
    def decorator(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            view = func(request, *args, **kwargs)
            paginator = Paginator(view, per_page)
            page_num = request.GET.get('page', 1)
            page = paginator.page(page_num)
            objects = page.object_list
            return result({
                "pager": {
                    "total": paginator.num_pages,
                    "next": page.next_page_number() if page.has_next() else None,
                    "previous": page.previous_page_number() if page.has_previous() else None,
                },
                "objects": list(map(lambda x: x.__dump__ if hasattr(x, "__dump__") else x, objects))
            })
        return _decorator
    return decorator


pagify = pager(10)
