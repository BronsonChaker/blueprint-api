from django.test import TestCase
from .models import Organisation
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

class OrganisationTestCase(TestCase):
    def test_create_org(self):
        org = Organisation.objects.create(
            name="Test Organisation",
            email_address="test@email.com",
            billing_address="123 Test Street, NSW, 2749",
            phone_number="0412345678",
        )

        self.assertEqual(org.name,"Test Organisation")
        self.assertEqual(org.email_address,"test@email.com")
        self.assertEqual(org.billing_address,"123 Test Street, NSW, 2749")
        self.assertEqual(org.phone_number,"0412345678")


