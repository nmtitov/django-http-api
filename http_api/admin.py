from django.contrib import admin

from .models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_filter = ("user__email", )
    ordering = ["created_at"]
    readonly_fields = ("token", "created_at", "last_seen_at", )
    search_fields = ["user__email"]
