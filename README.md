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
from django.views.decorators.csrf import csrf_exempt
from http_api.utils.data_structures import error, error_method_not_allowed, result
from http_api.utils.decorators import authentication_required, json_response


@csrf_exempt
@json_response
def index(request):
    if request.method == "GET":
        data = {
            "message": "It works!",
        }
        return result(data)
    else:
        return error_method_not_allowed()


@csrf_exempt
@json_response
@authentication_required
def user(request):
    if request.method == "GET":
        obj = request.user
        # Prepare response
        data = {
            "email": obj.email,
        }
        return result(data)
    else:
        return error_method_not_allowed()


@csrf_exempt
@json_response
def clients(request):
    if request.method == "GET":
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
        },
        return result(data, status=201)
    else:
        return error_method_not_allowed()
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
