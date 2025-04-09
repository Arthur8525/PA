from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['descricao', 'valor', 'data_vencimento', 'status']
        widgets = {
            'data_vencimento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
