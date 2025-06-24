from django import forms
from proyecto_ips_app.models import *

class EspecialidadFormulario(forms.ModelForm):
    class Meta:
        model=Especialidad
        fields=[
                'nombre_especialidad',
                'descripcion',
        ]
        widgets={
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }
