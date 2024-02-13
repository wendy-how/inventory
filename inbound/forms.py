
from django import forms
from .models import Inbound

class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = ['reference','date_received','product_sku', 'quantity', 'location', 'remarks']
