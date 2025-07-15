from django import forms
from proyecto_ips_app.models import *

class CitaFormulario(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha',
            'hora', 
            'medico', 
            'paciente', 
            'estado',
            'lugar_atencion',
            ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type':'time'})
        }
        