from django.db import models

class Document(models.Model):

    user_id = models.ForeignKey('users.user', on_delete=models.SET_NULL, null=True)
    job_id = models.ForeignKey('jobs.Job', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    file_type = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name
