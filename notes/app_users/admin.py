from django.contrib import admin

from app_users.models import NoteUser


@admin.register(NoteUser)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
        "last_login",

    )
    fields = (
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
        "last_login",
    )
    list_display_links = (
        "email",
    )
    search_fields = (
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
        "last_login",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
        "is_superuser",
    )
