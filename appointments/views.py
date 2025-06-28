# appointments/views.py
from rest_framework import generics, permissions
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated

class AppointmentListCreateView(generics.ListCreateAPIView):
    
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
       queryset = super().get_queryset()
       doctor_id = self.request.query_params.get('doctor;')
       patient_id = self.request.query_params.get('patient')
       date = self.request.query_params.get('date')

       if doctor_id:
           queryset = queryset.filter(doctor_id = doctor_id)
       if patient_id:
           queryset = queryset.filter(patient_id = patient_id)
       if date:
           queryset = queryset.filter(date=date)

       return queryset
    
    def perform_create(self, serializer):
        user = self.request.user
        if user.role not in ['DOCTOR', 'RECEPTIONIST']:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only doctors or receptionists can create appointments.")
        serializer.save()