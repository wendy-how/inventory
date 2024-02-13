from django import forms
from .models import Outbound

class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = ['reference','date_shipped','product_sku', 'quantity', 'destination', 'remarks']
