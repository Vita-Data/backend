# patients/urls.py

from django.urls import path
from .views import patient_summary  # or whatever view function you have

urlpatterns = [
    path('summary/', patient_summary),
]
