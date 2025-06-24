from django import forms
from proyecto_ips_app.models import *

class CitaMedicaFormulario(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = ['fecha', 'hora', 'medico', 'paciente', 'lugar']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
        