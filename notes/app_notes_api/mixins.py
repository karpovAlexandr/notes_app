from app_notes.models import Note


class OwnerAccessMixin:
    model = Note

    def __init__(self):
        self.request = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(user=self.request.user)
        return queryset
