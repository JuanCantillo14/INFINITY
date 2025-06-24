from django import forms
from proyecto_ips_app.models import *
from django.core.exceptions import ValidationError
import os

class AuxAdminFormulario(forms.ModelForm):
    class Meta:
        model= AuxAdmin
        fields=[
            # 'username', 
            'first_name', 
            'last_name', 
            'email' ,
            'telefono',
            'tipo_doc',
            'documento',
            'genero',
            'departamento',
            'ciudad',
            'fecha_nacimiento',
            'direccion',
            'imagen',
            'password', 
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'imagen':forms.FileInput()
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
        def validar_imagen(self):
            imagen = self.cleaned_data.get(imagen)

            if imagen:
                extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
                if extension not in ['jpg', 'png', 'jpeg']:
                    raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
                if imagen.size > 102400:
                    raise ValidationError('El tamaño máximo del archivo es 100 KB')
            return imagen
