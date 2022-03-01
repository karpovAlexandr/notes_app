from django import forms

from app_notes.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "title",
            "content",
            "is_published",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "off"}
            ),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
