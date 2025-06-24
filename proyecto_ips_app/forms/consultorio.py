from django import forms
from proyecto_ips_app.models import *


class ConsultorioFormulario(forms.ModelForm):
    class Meta:
        model= Consultorio
        fields=[
            'piso',
            'num_habitacion',
        ]
