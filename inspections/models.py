from django.db import models

class Inspection(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'

    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)
    inspector = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    template = models.ForeignKey('inspections.InspectionTemplate', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    inspection_date = models.DateField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.PENDING)

    def __str__ (self):
        return self.name
    
class InspectionTemplate(models.Model):
    organisaton = models.ForeignKey('organisations.Organisation', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name

class InspectionTemplateItem(models.Model):
    template = models.ForeignKey('inspections.InspectionTemplate', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order_num = models.PositiveIntegerField(default=0)

    def __str__ (self):
        return self.name
    
    
class Defect(models.Model):
    inspection = models.ForeignKey('inspections.Inspection', on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendors.Vendor', on_delete=models.SET_NULL, null=True, blank=True)
    job = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    room = models.ForeignKey('jobs.Room', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    photo_url = models.ImageField(upload_to='defects/', null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description
