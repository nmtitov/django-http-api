def result(data, status=200):
    return {
        "status_code": status,
        "result": data,
    }


def error(
    name,
    error_type=None,
    display_name=None,
    display_message=None,
    exception_info=None,
    status=555,
):
    return {
        "status_code": status,
        "error": {
            "name": name,
            "type": error_type,
            "display_name": display_name,
            "display_message": display_message,
            "exception_info": exception_info,
        },
    }
