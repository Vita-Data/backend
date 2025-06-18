# lab_reports/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.sample_report_view),  # change to actual view name
]
