Django HTTP API
===

Usage
---


1. Install `django-http-api` app from master branch: `pip install git+https://github.com/nmtitov/django-http-api@master` or add `-e git+https://github.com/nmtitov/django-http-api@master#egg=django-http-api` to your `requirements.txt` file and run `pip install -r requirements.txt`
2. Update your project `settings.py`

2.1. Turn off `Debug` if you want to have `JSON` responses everywhere

```
# Keep Debug = False to make sure we have the same logic in both development and production environments
# We need to set Debug = False to make custom error handlers defined in your_project.urls.py/http_api.views.error.py work
DEBUG = False
```

2.2. Add hosts to `ALLOWED_HOSTS`

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ]
```

2.3. Add `http_api` app to `INSTALLED_APPS`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'http_api',
]
```

2.4. Add `http_api.authentication_backend.SessionBackend` to `AUTHENTICATION_BACKENDS`

```
AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend', "http_api.authentication_backend.SessionBackend"]
```

2.5. Set `CSRF_FAILURE_VIEW`

```
CSRF_FAILURE_VIEW = "http_api.views.error.csrf_failure"
```

3. Define custom error handlers in `your_project.urls.py`

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use custom error handlers
handler400 = 'http_api.views.error.handler400'
handler403 = 'http_api.views.error.handler403'
handler404 = 'http_api.views.error.handler404'
handler500 = 'http_api.views.error.handler500'
```

4. Create a custom view in `your_app.views.py`. Here is an example. See https://github.com/nmtitov/django-http-api/blob/master/sample_project/sample_api/views.py

```
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_safe

from http_api.utils.data_structures import error, result
from http_api.views.decorators.api import require_auth, json


@csrf_exempt
@require_safe
@json
def index(request):
    return result({
        "message": "It works!",
    })


@csrf_exempt
@require_safe
@json
@require_auth
def user(request):
    obj = request.user
    # Prepare response
    email = obj.email if obj.email else None
    data = {
        "email": email,
    }
    return result(data)


@csrf_exempt
@require_safe
@json
def sample_error(request):
    return error("sample-error", error_type="sample_error", message="This is an example of erroneous response with a custom status code", status=520)


@csrf_exempt
@require_safe
@json
def sample_exception(request):
    raise SuspiciousOperation("sample_exception")


@csrf_exempt
@require_http_methods(["GET", "HEAD", "POST"])
@json
def clients(request):
    if request.method == "GET" or request.method == "HEAD":
        data = [{
            "first_name": "Nikita",
            "last_name": "Titov",
            "email": "nmtitov@ya.ru",
            "github": "https://github.com/nmtitov",
        }, {
            "first_name": "Nikita",
            "last_name": "Titov",
            "email": "nmtitov@ya.ru",
            "github": "https://github.com/nmtitov",
        }, {
            "first_name": "Nikita",
            "last_name": "Titov",
            "email": "nmtitov@ya.ru",
            "github": "https://github.com/nmtitov",
        }]
        return result(data)
    elif request.method == "POST":
        data = {
            "first_name": "Nikita",
            "last_name": "Titov",
            "email": "nmtitov@ya.ru",
            "github": "https://github.com/nmtitov",
        }
        return result(data, status=201)
    else:
        return None


@csrf_exempt
@require_safe
@json
@require_auth
def secret(request):
    return result({"message": "This is my secret"})


# Empty response
@csrf_exempt
@json
def empty(request):
    return None


# Empty response with a custom status code
@csrf_exempt
@json
def empty_status(request):
    return {
        "status_code": 404,
        "body": None,
    }


# List response
@csrf_exempt
@require_safe
@json
def greetings(request):
    return [{
        "language": "English",
        "greeting": "Hello",
    }, {
        "language": "French",
        "greeting": "Bonjour",
    }, {
        "language": "Spanish",
        "greeting": "Hola",
    }, {
        "language": "German",
        "greeting": "Hallo",
    }, {
        "language": "Italian",
        "greeting": "Ciao",
    }, {
        "language": "Portugese",
        "greeting": "Ola",
    }]


# A plain dict response with a custom structure (keep in mind that "status_code" and "body" keys are reserved)
@csrf_exempt
@require_safe
@json
def united_states(request):
    return {
        "country": "United States",
        "capital": "Washington, D.C.",
        "largest_city": "New York City",
        "national_language": "English",
        "area": "9833520",
    }

```

5. Add url paths to your views in `your_app.urls.py`

```
from django.urls import path
from . import views

urlpatterns = [
    path('clients', views.clients, name='clients'),
    path('secret', views.secret, name='secret'),
    path('user', views.user, name='user'),
]
```

6. Update `your_project.urls.py` and include urls from `your_app.urls.py`

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app.urls')),
]
```

7. Run migrations

`python manage.py migrate`

8. In order to make `runserver` serve static files for admin panel with `Debug = False`, run local server with `python manage.py runserver --insecure`
