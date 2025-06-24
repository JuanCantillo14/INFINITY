from django import forms
from proyecto_ips_app.models import *

class LugarAtencionFormulario(forms.ModelForm):
    class Meta:
        model=LugarAtencion
        fields=[
            'nombre_lugar',
            'direccion_lugar',
            'departamento',
            'ciudad',
        ]
        widgets = {
            'departamento': forms.Select(attrs={'id': 'id_departamento'}),
            'ciudad': forms.Select(attrs={'id': 'id_ciudad'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['ciudad'].queryset = Ciudad.objects.none()

            if 'departamento' in self.data:
                try:
                    departamento_id = self.data.get('departamento')
                    self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento_id=departamento_id)
                except:
                    pass
            elif self.instance.pk and self.instance.departamento:
                self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento=self.instance.departamento)
