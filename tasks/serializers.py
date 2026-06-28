from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['job', 'vendor', 'name', 'booking_date', 'completion_date', 'status']