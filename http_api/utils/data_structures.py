def result(data, status=200):
    return {
        "status_code": status,
        "body": {
            "result": data,
        }
    }


def error(name, error_type=None, display_name=None, display_message=None, exception_info=None, status=520):
    return {
        "status_code": status,
        "body": {
            "error": {
                "name": name,
                "type": error_type,
                "display_name": display_name,
                "display_message": display_message,
                "exception_info": exception_info,
            }
        },
    }
