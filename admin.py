from django.contrib import admin
from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_filter = ("user__email", )
    ordering = ["created_at"]
    readonly_fields = ("token", "created_at", "used_at", )
    search_fields = ["user__email"]

