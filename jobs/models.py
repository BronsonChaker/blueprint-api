import uuid
from django.db import models

class Job(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACTIVE = 'active', 'Active'
        ON_HOLD = 'on_hold', 'ON_HOLD'
        FINALISED = 'finalised', 'Finalised'
        COMPLETED = 'completed', 'Completed'

    class Stage(models.TextChoices):
        SALES = 'sales', 'Sales'
        PRE_CONSTRUCTION = 'pre-construction', 'Pre-Construction'
        CONSTRUCTION = 'construction', 'Construction'
        COMPLETION = 'completion', 'Completion'
        MAINTENANCE = 'maintenance', 'Maintenance'


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_number = models.CharField(max_length=10, null=True, blank=True)
    job_reference = models.UUIDField(default=uuid.uuid4, editable=False)
    organisation = models.ForeignKey('organisations.Organisation', on_delete=models.CASCADE)
    supervisor = models.ForeignKey('users.user', on_delete=models.SET_NULL, null=True)
    template = models.ForeignKey('jobs.JobTemplate', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, null=False)
    stage = models.CharField(max_length=20, choices=Stage.choices, null=False)
    client_name = models.CharField(max_length=255, blank=True)
    client_email = models.EmailField(blank=True)
    client_phone = models.CharField(max_length=20, blank=True)
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    construction_start_date = models.DateField(null=True, blank=True)
    construction_end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class JobTemplate(models.Model):
    organisation = models.ForeignKey('organisations.Organisation', on_delete=models.CASCADE)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class JobTemplateItem(models.Model):
    template_id = models.ForeignKey('jobs.JobTemplate', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order_num = models.PositiveIntegerField(default=0)

    def __str__ (self):
        return self.name
    
class Room(models.Model):
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
