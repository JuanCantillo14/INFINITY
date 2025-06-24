from django import forms
from proyecto_ips_app.models import *

class CiudadFormulario(forms.ModelForm):
    class Meta:
        model= Ciudad
        fields=[
            'codigo_municipio',
            'nombre_ciudad',
            'codigo_departamento',
        ]
