from django.test import TestCase
from .models import Job

class JobTestCase(TestCase):
    def test_create_job(self):
        job = Job.objects.create(
            
        )