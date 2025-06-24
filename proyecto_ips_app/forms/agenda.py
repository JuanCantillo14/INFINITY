from django import forms
from proyecto_ips_app.models import *

class AgendaFormulario(forms.ModelForm):
    class Meta: 
        model=Agenda
        fields=[
            'medico',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'fecha_creacion',
        ]

