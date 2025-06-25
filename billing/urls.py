from django.urls import path
from .views import BillListCreateView, BillDetailView

urlpatterns = [
    path('bills/', BillListCreateView.as_view(), name='bill-list-create'),         
    path('bills/<str:bill_number>/', BillDetailView.as_view(), name='bill-detail'), 
]
