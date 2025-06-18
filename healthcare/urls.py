# healthcare/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('patients.urls')),
    path('api/', include('appointments.urls')),
    path('api/', include('lab_reports.urls')),
    path('api/', include('billing.urls')),
    path('api/', include('dashboard.urls')),
]
