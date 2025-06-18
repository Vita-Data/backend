# billing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_billing),  # just a dummy endpoint
]
