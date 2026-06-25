from django.db import models

class Inspection(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'

    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)
    inspector = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    # TODO: Add template_id
    name = models.CharField(max_length=255)
    inspection_date = models.DateField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING)

    def __str__ (self):
        return self.name
