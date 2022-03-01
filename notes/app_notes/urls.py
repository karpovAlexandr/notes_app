from django.urls import path

from app_notes import views

app_name = "note"

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_list'),
    path('note_create/', views.NoteCreateView.as_view(), name='note_create'),
    path('<int:pk>', views.NoteDetailView.as_view(), name='note_detail'),
    path('<int:pk>/update', views.NoteUpdateView.as_view(), name='note_update'),
]
