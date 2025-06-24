from django.db import models
from patients.models import Patient

class LabTestReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('scheduled', 'Scheduled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    result = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)
    report_file = models.FileField(upload_to='reports/', blank=True, null=True)

    def __str__(self):
        return f"{self.patient.name} - {self.test_type}"
