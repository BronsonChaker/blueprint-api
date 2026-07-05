from rest_framework import serializers
from .models import *
from tasks.serializers import TaskSerializer

class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Job
        fields = [
            'id',
            'job_number',
            'job_reference',
            'organisation',
            'supervisor',
            'template',
            'name',
            'address',
            'status',
            'stage',
            'client_name',
            'client_email',
            'client_phone',
            'contract_start_date',
            'contract_end_date',
            'construction_start_date',
            'construction_end_date',
            'tasks'
            ]