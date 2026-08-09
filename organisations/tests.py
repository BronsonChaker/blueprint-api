from django.test import TestCase
from .models import Organisation
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

class OrganisationTestCase(TestCase):
    def organisation_set_up(self):
        
