# billing/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer

@api_view(['GET'])
def test_billing(request):
    return Response({"message": "Billing module working"})



class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDetailView(generics.RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'bill_number'
