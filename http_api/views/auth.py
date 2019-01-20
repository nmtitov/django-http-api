from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from ..models import Session
from ..utils.data_structures import error, result
from ..views.decorators.api import json


@csrf_exempt
@require_POST
@json
def signup(request):
    # Receive params
    email = str(request.POST["email"])
    password = str(request.POST["password"])
    # Create object
    user_model = get_user_model()
    obj = user_model.objects.create_user(email=email, password=password)
    # Prepare response
    data = {
        "email": obj.email,
    }
    return result(data, status=201)


@csrf_exempt
@require_POST
@json
def signin(request):
    # Receive params
    email = str(request.POST["email"])
    password = str(request.POST["password"])
    # Check password
    user_model = get_user_model()
    user = user_model.objects.get(email=email)
    if not user.check_password(password):
        return error("Invalid password", error_type="check_password", message="Password is invalid", status=400)
    # Create session object
    session = Session.objects.create(user=user)
    # Prepare response
    data = {
        "token": session.token,
    }
    return result(data, status=201)
