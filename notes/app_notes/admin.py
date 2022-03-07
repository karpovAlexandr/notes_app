from django.contrib import admin

from app_notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "user",
        "created_at",
        "updated_at",
        "is_published",
    )
    fields = (
        "title",
        "content",
        "user",
        "created_at",
        "updated_at",
        "is_published",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = (
        "id",
        "title",
        "content",
        "user",
        "created_at",
        "updated_at",
        "is_published",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )

