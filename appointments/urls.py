# appointments/urls.py

from django.urls import path
from .views import appointments_handler

urlpatterns = [
    path('appointments/', appointments_handler),  # POST, GET, filter by doctor/patient/date
]
