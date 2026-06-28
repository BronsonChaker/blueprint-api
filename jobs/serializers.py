from rest_framework import serializers
from .models import *
from tasks.serializers import TaskSerializer

class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = ['id', 'job_number', 'organisation', 'address', 'status', 'stage', 'tasks']