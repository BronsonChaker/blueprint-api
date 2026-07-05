from django.urls import path
from . import views

app_name = 'documents'
urlpatterns = [
    path('', views.document_list),
    path('create', views.create_document)
]