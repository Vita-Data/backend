from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient, LabTestReport
from .serializers import PatientSerializer, LabTestReportSerializer
from .permissions import LabReportPermission

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [LabReportPermission]

class LabTestReportViewSet(viewsets.ModelViewSet):
    queryset = LabTestReport.objects.all()
    serializer_class = LabTestReportSerializer
    permission_classes = [LabReportPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['report_date', 'status', 'patient']
    search_fields = ['patient__name', 'test_type']
