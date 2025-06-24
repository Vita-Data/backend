from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient, LabTestReport
from .serializers import PatientSerializer, LabTestReportSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class LabTestReportViewSet(viewsets.ModelViewSet):
    queryset = LabTestReport.objects.all()
    serializer_class = LabTestReportSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['report_date', 'status', 'patient']
    search_fields = ['patient__name', 'test_type']
