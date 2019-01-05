from django.contrib import admin
from .models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    readonly_fields=('value', 'created_at', 'used_at', )

