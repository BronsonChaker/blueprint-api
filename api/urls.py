from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_organisations, name='add_organisation'),
    path('all/', views.view_organisations, name='view_organisations')
]