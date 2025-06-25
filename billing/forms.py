from django import forms
from .models import Bill

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('bill_number',  'bill_amount', 'bill_status')  