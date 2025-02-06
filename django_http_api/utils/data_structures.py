def result(data, status=200):
    return {
        "s": status,
        "r": data,
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
        "s": status,
        "e": {
            "name": name,
            "type": error_type,
            "display_name": display_name,
            "display_message": display_message,
            "exception_info": exception_info,
        },
    }
