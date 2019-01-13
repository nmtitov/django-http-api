def result(data, status=200):
    return {
        "status_code": status,
        "body": {
            "result": data,
        }
    }


def error(name, error_type=None, message=None, exception=None, status=520):
    return {
        "status_code": status,
        "body": {
            "error": {
                "name": name,
                "type": error_type,
                "message": message,
                "exception": exception,
            }
        },
    }


def error_method_not_allowed():
    return error("method-not-allowed", error_type="method-not-allowed", status=405)
