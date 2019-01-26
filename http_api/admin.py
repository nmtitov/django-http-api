from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Session

user_model = get_user_model()
username_field = "user__{username_field}".format(username_field=user_model.USERNAME_FIELD)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_filter = (username_field, )
    ordering = ["created_at"]
    readonly_fields = ("token", "created_at", "last_seen_at", )
    search_fields = [username_field]
