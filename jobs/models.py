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
        PRE_CONSTRUCTION = 'pre-construciton', 'Pre-Construction'
        CONSTRUCTION = 'construction', 'Construction'
        COMPLETION = 'completion', 'Completion'
        MAINTENANCE = 'maintenance', 'Maintenance'

    organisation = models.ForeignKey('organisations.Organisation', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, null=False)
    stage = models.CharField(max_length=20, choices=Stage.choices, null=False)
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    construction_start_date = models.DateField(null=True, blank=True)
    construction_start_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

