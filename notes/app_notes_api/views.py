from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app_notes_api import serializers

from app_notes_api.mixins import OwnerAccessMixin


class ListNote(OwnerAccessMixin, generics.ListAPIView):
    serializer_class = serializers.NoteListSerializer
    permission_classes = (IsAuthenticated,)


class DetailNote(OwnerAccessMixin, generics.RetrieveAPIView):
    serializer_class = serializers.NoteDetailSerializer
    permission_classes = (IsAuthenticated,)


class CreateNote(OwnerAccessMixin, generics.CreateAPIView):
    serializer_class = serializers.NoteCreateSerializer
    permission_classes = (IsAuthenticated,)


class UpdateNote(OwnerAccessMixin, generics.UpdateAPIView):
    serializer_class = serializers.NoteUpdateSerializer
    permission_classes = (IsAuthenticated,)


class DeleteNote(OwnerAccessMixin, generics.DestroyAPIView):
    serializer_class = serializers.NoteDeleteSerializer
    permission_classes = (IsAuthenticated,)
