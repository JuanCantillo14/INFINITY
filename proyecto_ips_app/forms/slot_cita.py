from django import forms
from proyecto_ips_app.models import *

class SlotCita(forms.ModelForm):
    class Meta:
        model = SlotCita
        fields=[
            'agenda',
            'fehca',
            'hora_inicio',
            'ocupado',
            'paciente', 
        ]
        widgets={
            'fecha':forms.DateInput(attrs={'type':'date'}),
                
        }
        
    