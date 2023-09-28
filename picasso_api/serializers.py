from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ['id','file', 'uploaded_at', 'file', 'processed']
        read_only_fields = ['id', 'uploaded_at', 'processed']
