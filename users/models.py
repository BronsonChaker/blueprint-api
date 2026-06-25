from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
    
class Membership(models.Model):
    """Gives a user from an organisation a role."""

    class Role(models.TextChoices):
        OWNER = 'owner', 'Owner'
        ADMIN = 'admin', 'Admin'
        SUPERVISOR = 'supervisor', 'Supervisor'
        INSPECTOR = 'inspector', 'Inspector'
        GUEST = 'guest', 'Guest'

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    organisation = models.ForeignKey('organisations.Organisation', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: unique_together = ('user', 'organisation')

    def __str__(self):
        return f"{self.user} @ {self.organisation} ({self.role})"




