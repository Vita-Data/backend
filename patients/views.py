# patients/views.py

from rest_framework import viewsets, mixins
from .models import Patient
from .serializers import PatientSerializer
from .permissions import Permission

class PatientViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
        
        """
        Allows cresting and listing patiens with (restricted to DOCTOR and RECEPTIOIST)
        """
        
        queryset = Patient.objects.all()
        serializer_class = PatientSerializer
        permission_classes = [Permission]