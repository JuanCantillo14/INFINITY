from django import forms
from proyecto_ips_app.models import *

class GrupoIngresosFormulario(forms.ModelForm):
    class Meta:
        model=GrupoIngresos
        fields=[
            'nivel_ingresos',
            'valor',
            'descripcion',
        ]
        