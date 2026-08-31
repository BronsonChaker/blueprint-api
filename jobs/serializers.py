from rest_framework import serializers
from .models import *
from tasks.serializers import TaskSerializer
from users.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    supervisor_first_name = serializers.CharField(source='supervisor.first_name', read_only=True)
    supervisor_last_name = serializers.CharField(source='supervisor.last_name', read_only=True)
    class Meta:
        model = Job
        fields = [
            'id',
            'job_number',
            'job_reference',
            'organisation',
            'supervisor',
            'template',
            'supervisor_first_name',
            'supervisor_last_name',
            'template',
            'name',
            'address',
            'status',
            'stage',
            'client_first_name',
            'client_last_name',
            'client_email',
            'client_phone',
            'client_billing',
            'contract_start_date',
            'contract_end_date',
            'contract_price',
            'construction_start_date',
            'construction_end_date',
            'tasks'
            ]