from rest_framework import serializers
from .models import Patient, LabTestReport

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class LabTestReportSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)

    class Meta:
        model = LabTestReport
        fields = '__all__'
