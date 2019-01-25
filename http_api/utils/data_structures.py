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
