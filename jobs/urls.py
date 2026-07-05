from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.user_job_list),
    path('create', views.create_job),
    path('<uuid:pk>/completed-tasks/', views.filter_tasks_completed),
    path('<uuid:pk>/not-completed-tasks/', views.filter_tasks_not_completed),
]

urlpatterns = format_suffix_patterns(urlpatterns)