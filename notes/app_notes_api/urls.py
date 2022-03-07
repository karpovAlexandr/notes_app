from django.urls import path
from app_notes_api import views


app_name = 'note_api'

urlpatterns = [
    path('notes/', views.ListNote.as_view(), name='note_list'),
    path('notes/add/', views.CreateNote.as_view(), name='note_create'),
    path('notes/<int:pk>/', views.DetailNote.as_view(), name='note_detail'),
    path('notes/<int:pk>/update/', views.UpdateNote.as_view(), name='note_update'),
    path('notes/<int:pk>/delete/', views.DeleteNote.as_view(), name='note_delete'),
]
