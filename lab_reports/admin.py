from django.contrib import admin
from .models import Patient, LabTestReport

admin.site.register(Patient)
admin.site.register(LabTestReport)
