from django.test import TestCase
from .models import Job
from organisations.models import Organisation
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()
class JobTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="test",
            email="test@example.com",
            password="testpassword1"
        )
        self.organisation = Organisation.objects.create(
            name = "Test Organisation"
        )

    def test_create_job(self):
        job = Job.objects.create(
            job_number = "12345",
            organisation = self.organisation,
            supervisor = self.user,
            name="123 Test Street, Test, NSW, 1234",
            address="123 Test Street, Test, NSW, 1234",
        )

        self.assertEqual(job.job_number, "12345")
        self.assertEqual(job.organisation, self.organisation)
        self.assertEqual(job.supervisor, self.user)
        self.assertEqual(job.name, "123 Test Street, Test, NSW, 1234")
        self.assertEqual(job.address, "123 Test Street, Test, NSW, 1234")

    def test_create_job_no_org_fails(self):
    
        job = Job.objects.create(
            job_number = "12345",
            supervisor = self.user,
            name="123 Test Street, Test, NSW, 1234",
            address="123 Test Street, Test, NSW, 1234",
        )

        self.assertEqual(job.job_number, "12345")
        self.assertEqual(job.supervisor, self.user)
        self.assertEqual(job.name, "123 Test Street, Test, NSW, 1234")
        self.assertEqual(job.address, "123 Test Street, Test, NSW, 1234")
        