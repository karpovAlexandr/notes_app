from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic, View

from app_notes.forms import NoteForm
from app_notes.models import Note


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        if self.request.user.is_authenticated:
            notes_count = Note.objects.filter(user=self.request.user).count()
            context.update(notes_count=notes_count)
        return render(request, "index.html", context)


class NoteListView(LoginRequiredMixin, generic.ListView):
    def get_queryset(self):
        return (
            Note.objects.filter(is_published=True, user=self.request.user)
            .select_related("user")
            .only("title", "content", "created_at", "user")
            .order_by("-created_at")
        )


class NoteCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    form_class = NoteForm
    template_name = 'app_notes/note_form.html'

    def form_valid(self, form):
        form.instance.user_id = getattr(self.request.user, "id")
        return super().form_valid(form)


class NoteDetailView(
    LoginRequiredMixin,
    generic.DetailView
):
    context_object_name = 'note'
    model = Note
    queryset = Note.objects.filter(is_published=True).select_related("user").only("title", "content", "created_at", "updated_at", "user")


class NoteUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    form_class = NoteForm
    queryset = Note.objects.filter(is_published=True)
