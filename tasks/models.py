from django.db import models

class Task(models.Model):
    class Status(models.TextChoices):
        NOT_COMPLETE = 'not complete', 'Not Complete'
        COMPLETED = 'completed', 'Completed'

    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    booking_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name