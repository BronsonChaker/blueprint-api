from django.db.models import fields
from rest_framework import serializers
from organisations.models import Organisation

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('id', 'name', 'email_address', 'billing_address', 'phone_number', 'created_at')
