# appointments/urls.py

from django.urls import path
from .views import AppointmentListCreateView

urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name = 'appointments'),  # POST, GET, filter by doctor/patient/date
]
