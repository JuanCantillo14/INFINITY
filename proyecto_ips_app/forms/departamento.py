from django import forms
from proyecto_ips_app.models import *

class DepartamentoFormulario(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=[
            'codigo_departamento',
            'nombre_departamento',
        ]
