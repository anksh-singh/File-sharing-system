from rest_framework import serializers
from .models import OpsCliUsers, UploadFile

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpsCliUsers
        fields = ('username', 'password', 'user_type')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = ('file', 'uploaded_by')