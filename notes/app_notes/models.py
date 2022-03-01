
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from app_users.models import NoteUser


class Note(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    content = models.TextField(_('Content'), max_length=50)
    user = models.ForeignKey(NoteUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    is_published = models.BooleanField(_('Published'), default=True)

    objects = models.Manager()

    def __str__(self):
        return f'{self.title}, {self.created_at}, {self.is_published}'

    @staticmethod
    def get_absolute_url():
        return reverse('note:note_list')

    class Meta:
        verbose_name = _('Note')
        verbose_name_plural = _('Notes')

