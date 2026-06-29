from rest_framework import serializers
from .models import *

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'user_id',
            'job_id',
            'name',
            'description',
            'url',
            'upload_date',
            'file_type'
        ]