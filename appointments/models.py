from django.db import models
from patients.models import Patient
from users.models import CustomUser

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ] # Defines the choices for appointment status

    patient = models.ForeignKey(
        Patient,
        on_delete = models.CASCADE,
        related_name = 'appointments'
        )
    doctor = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        limit_choices_to = {'role' : 'DOCTOR'},
        related_name = 'appointments'
    )
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SCHEDULED'
    )
    issue = models.TextField(
        blank = True,
        help_text = "Brief description of patient's issue or reason to visit"
    )
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Appointment: {self.patient.name} with {self.doctor.email} on {self.date} at {self.time}"
