from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.users_list),
    path("memberships/", views.membership_list),
    path('api-auth/', include('rest_framework.urls'))

]

urlpatterns = format_suffix_patterns(urlpatterns)
