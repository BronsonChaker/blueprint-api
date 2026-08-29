from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Task(models.Model):
    class Status(models.TextChoices):
        NOT_COMPLETE = 'not complete', 'Not Complete'
        COMPLETED = 'completed', 'Completed'

    class TaskType(models.TextChoices):
        INSPECTION = 'Inpsection', 'Inpsection'
        CLAIM = 'claim', 'Claim'
        SAFETY = 'safety', 'Safety'
        ACTIVITY = 'activity', 'Activity'

    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE, related_name='tasks')
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    task_type = models.CharField(choices=TaskType.choices, null=False, max_length=20, default="activity")
    duration = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    booking_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, null=False)
    is_critical = models.BooleanField(default=False,blank=True)
    is_milestone = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name