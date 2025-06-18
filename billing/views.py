# billing/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_billing(request):
    return Response({"message": "Billing module working"})
