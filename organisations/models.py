import uuid
from django.db import models

class Organisation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    display_picture = models.ImageField(upload_to='organisations/', null=True, blank=True)
    email_address = models.EmailField(blank=True)
    billing_address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

# TODO: to be migrated into DB
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['user', 'organisation'], name='unique_user_org')
    #     ]

    def __str__(self):
        return self.name