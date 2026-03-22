from django import forms
from .models import Eleccion

class EleccionForm(forms.ModelForm):
    class Meta:
        model  = Eleccion
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_cierre', 'estado']
        widgets = {
            'nombre':       forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':  forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado':       forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        inicio = cleaned_data.get('fecha_inicio')
        cierre = cleaned_data.get('fecha_cierre')
        if inicio and cierre and cierre <= inicio:
            raise forms.ValidationError("La fecha de cierre debe ser posterior al inicio.")
        return cleaned_data