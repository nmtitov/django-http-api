try:
    from secrets import token_hex
except ImportError:
    from os import urandom


    def token_hex(nbytes=None):
        return urandom(nbytes).hex()

from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Session(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    token = models.CharField(max_length=64, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_seen_at = models.DateTimeField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.token = token_hex(32)
        super().save(*args, **kwargs)

    def update_last_seen(self):
        self.last_seen_at = now()

    def __str__(self):
        return getattr(self.user, self.user.USERNAME_FIELD)
