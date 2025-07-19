from django import forms
from .models import ComprobantePago

class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = ComprobantePago
        fields = ['estudiante', 'archivo']
