# appointments/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def appointments_handler(request):
    return Response({"message": "Appointments endpoint placeholder"})
