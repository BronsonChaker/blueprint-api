from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    job_address = serializers.CharField(source='job.address', read_only=True)
    job_number = serializers.CharField(source='job.job_number', read_only=True)
    class Meta:
        model = Task
        fields = ['job', 'job_address', 'job_number', 'vendor_name', 'name', 'task_type', 'duration', 'booking_date', 'completion_date', 'status', 'is_critical', 'is_milestone']