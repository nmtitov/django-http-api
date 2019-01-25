from sys import exc_info
from traceback import format_exc


def get_exception_info():
    exc_type, value, traceback = exc_info()
    if exc_type and value and traceback:
        return {
            "name": "{module}.{name}".format(module=exc_type.__module__, name=exc_type.__name__),
            "value": str(value),
            "repr": repr(value),
            "stacktrace": format_exc().splitlines(),
        }
    else:
        return None
