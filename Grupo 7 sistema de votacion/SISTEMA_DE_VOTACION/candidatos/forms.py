from django import forms
from .models import Candidato

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nombre', 'eleccion']
        widgets = {
            'nombre':   forms.TextInput(attrs={'class': 'form-control'}),
            'eleccion': forms.Select(attrs={'class': 'form-select'}),
        }