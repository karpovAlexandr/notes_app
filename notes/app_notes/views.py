import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View
from django.utils.translation import gettext_lazy as _

from app_notes.forms import NoteForm
from app_notes.models import Note

logger = logging.getLogger(__name__)


def handler403(request, exception):
    logger.error(exception)
    return HttpResponseRedirect('/notes')


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
    queryset = (
        Note.objects.filter(is_published=True)
            .select_related("user")
            .only(
            "title", "content", "created_at", "updated_at", "user"
        )
    )

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        current_user = self.request.user
        if self.object.user != current_user and not current_user.is_superuser:
            raise PermissionDenied(_('You can read only your Note!'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class NoteUpdateView(
    LoginRequiredMixin,
    generic.UpdateView
):
    form_class = NoteForm
    queryset = Note.objects.filter(is_published=True)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        current_user = self.request.user
        if self.object.user != current_user and not current_user.is_superuser:
            raise PermissionDenied(_('You can update only your Note!'))
        return super().get(request, *args, **kwargs)


class NoteDeleteView(
    LoginRequiredMixin,
    generic.DeleteView
):
    model = Note

    def get_success_url(self):
        return reverse('note:note_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        current_user = self.request.user
        if self.object.user != current_user and not current_user.is_superuser:
            raise PermissionDenied(_('You can delete only your Note!'))
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
