from django.db import models
from django.utils import timezone




class Bill(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
        ('Pending', 'Pending'),
    ]

    bill_number = models.CharField(max_length=20, primary_key=True)
    patient_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill_date = models.DateField(default=timezone.now)
    
    # patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    # appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE)

    def __str__(self):
        return f"Bill #{self.bill_number} for {self.patient}"

