from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            'organisation',
            'name',
            'email',
            'phone_number',
            'business_number',
            'contact_name',
            'business_address'
            ]