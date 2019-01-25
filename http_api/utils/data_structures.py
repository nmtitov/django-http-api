from django.core.paginator import EmptyPage, Paginator


def result(data, status=200):
    return {
        "status_code": status,
        "body": {
            "result": data,
        }
    }


def error(name, error_type=None, message=None, exception_info=None, status=520):
    return {
        "status_code": status,
        "body": {
            "error": {
                "name": name,
                "type": error_type,
                "message": message,
                "exception_info": exception_info,
            }
        },
    }


def pager(objects, fn=None, per_page=10, current_page=1):
    try:
        paginator = Paginator(objects, per_page)
        page_objects = paginator.get_page(current_page)
        page = paginator.page(current_page)
        return result({
            "pager": {
                "total": paginator.num_pages,
                "next": page.next_page_number() if page.has_next() else None,
                "previous": page.previous_page_number() if page.has_previous() else None,
            },
            "items": list(map(fn, page_objects)) if fn else page_objects
        })
    except EmptyPage as e:
        return error("empty-page", error_type="pager", message="The requested page is empty", exception_info=None, status=404)
