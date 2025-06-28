from django.contrib import admin
from .models import Appointment  # <-- Import the model

# Register the model
admin.site.register(Appointment)
