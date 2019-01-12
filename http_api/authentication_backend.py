from django.contrib.auth import get_user_model
from .models import Session


class SessionBackend:
    @staticmethod
    def authenticate(request, token=None):
        try:
            session = Session.objects.get(token=token)
            session.update_last_seen()
            session.save()
            return session.user
        except Session.DoesNotExist:
            return None

    @staticmethod
    def get_user(user_id):
        user = get_user_model()
        try:
            return user.objects.get(pk=user_id)
        except user.DoesNotExist:
            return None
