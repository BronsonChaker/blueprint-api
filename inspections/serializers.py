from rest_framework import serializers
from .models import *

class DefectSerializer(serializers.ModelSerializer):
    vendor_name = serializers.CharField(source='vendor.name', read_only=True)
    class Meta:
        model = Defect
        fields = [
            'inspection',
            'vendor_name',
            'job',
            'room',
            'description',
            'photo_url',
            'is_completed',
        ]
class InspectionSerializer(serializers.ModelSerializer):
    defects = DefectSerializer(many=True, read_only=True)
    class Meta:
        model = Inspection
        fields = [
            'job', 
            'task', 
            'inspector', 
            'template', 
            'name',
            'inspection_date',
            'uploaded_at',
            'status',
            'defects'
            ]