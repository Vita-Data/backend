# lab_reports/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def sample_report_view(request):
    return Response({"message": "Lab report placeholder"})
