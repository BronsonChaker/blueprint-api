from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.user_job_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)