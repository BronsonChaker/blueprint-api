from django.contrib import admin
from .models import *

admin.site.register(Inspection)
admin.site.register(InspectionTemplate)
admin.site.register(InspectionTemplateItem)
admin.site.register(Defect)
