from rest_framework import serializers
from .models import Task
from vendors.models import Vendor

class TaskSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    class Meta:
        model = Task
        fields = ['job', 'vendor_name', 'name', 'booking_date', 'completion_date', 'status']