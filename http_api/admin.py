from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Session

username_field = f"user__{get_user_model().USERNAME_FIELD}"


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "created_at", "last_seen_at", )
    list_filter = ("created_at", "last_seen_at", )
    ordering = ["-created_at"]
    readonly_fields = ("id", "token", "created_at", "last_seen_at", )
    search_fields = (username_field, "token", )
