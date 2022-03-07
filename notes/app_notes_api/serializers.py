from rest_framework import serializers

from app_notes.models import Note


class NoteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class NoteDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'


class NoteCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Note
        fields = '__all__'

    def create(self, validated_data):
        return Note.objects.create(**validated_data)


class NoteUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = (
            'title',
            'content',
            'is_published',
        )


class NoteDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'
