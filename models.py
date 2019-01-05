from django.conf import settings
from django.db import models
from secrets import token_hex


class Token(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    value = models.CharField(max_length=255, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    used_at = models.DateTimeField(blank=True, null=True, editable=False)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.value = token_hex()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.value
