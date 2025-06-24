from django import forms
from proyecto_ips_app.models import *

class EstadoCitaFormulario(forms.ModelForm):
    class Meta:
        model=EstadoCita
        fields=[
            'nombre_estado',
            'descripcion'
        ]
