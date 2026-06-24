from django.db import models

# Create your models here.
class Vendor(models.Model):
    organisation = models.ForeignKey('organisations.Organisation', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    business_number = models.CharField(max_length=20, blank=True)
    contact_name = models.CharField(max_length=50, blank=True)
    business_address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

