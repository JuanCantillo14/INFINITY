# from django import forms
# from proyecto_ips_app.models import *
# from django.core.exceptions import ValidationError
# import os

# class UsuarioFormulario(forms.ModelForm):
#     class Meta:
#         model= Usuario
#         fields=[
#             # 'username', 
#             'rol',
#             'first_name', 
#             'last_name', 
#             'email' ,
#             'telefono',
#             'tipo_doc',
#             'documento',
#             'genero',
#             'departamento',
#             'ciudad',
#             'fecha_nacimiento',
#             'direccion',
#             'imagen',
#             'password', 
#         ]
        
#         widgets= {
#             'password': forms.PasswordInput(),
#             'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
#             'imagen':forms.FileInput()
#         }
        
#         def validar_imagen(self):
#             imagen = self.cleaned_data.get(imagen)

#             if imagen:
#                 extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
#                 if extension not in ['jpg', 'png', 'jpeg']:
#                     raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
#                 if imagen.size > 102400:
#                     raise ValidationError('El tamaño máximo del archivo es 100 KB')
#             return imagen
        
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['ciudad'].queryset = Ciudad.objects.none()

#             if 'departamento' in self.data:
#                 try:
#                     departamento_id = self.data.get('departamento')
#                     self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento_id=departamento_id)
#                 except:
#                     pass
#             elif self.instance.pk and self.instance.departamento:
#                 self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento=self.instance.departamento)

# class PacienteFormulario(forms.ModelForm):
#     class Meta:
#         model= Paciente
#         fields=[
#             # 'username', 
#             'first_name', 
#             'last_name', 
#             'email' ,
#             'telefono',
#             'tipo_doc',
#             'documento',
#             'genero',
#             'departamento',
#             'ciudad',
#             'fecha_nacimiento',
#             'direccion',
#             'imagen',
#             'eps',
#             'tipo_regimen',
#             'ocupacion',
#             'grupo_ingresos',
#             'password', 
            
#         ]
#         widgets= {
#             'password': forms.PasswordInput(),
#             'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
#             'imagen':forms.FileInput()
#         }
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['ciudad'].queryset = Ciudad.objects.none()

#             if 'departamento' in self.data:
#                 try:
#                     departamento_id = self.data.get('departamento')
#                     self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento_id=departamento_id)
#                 except:
#                     pass
#             elif self.instance.pk and self.instance.departamento:
#                 self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento=self.instance.departamento)
        
#         def validar_imagen(self):
#             imagen = self.cleaned_data.get(imagen)

#             if imagen:
#                 extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
#                 if extension not in ['jpg', 'png', 'jpeg']:
#                     raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
#                 if imagen.size > 102400:
#                     raise ValidationError('El tamaño máximo del archivo es 100 KB')
#             return imagen

        

# class MedicoFormulario(forms.ModelForm):
#     class Meta:
#         model= Medico
#         fields= [
#             # 'username', 
#             'first_name', 
#             'last_name', 
#             'email' ,
#             'telefono',
#             'tipo_doc',
#             'documento',
#             'genero',
#             'departamento',
#             'ciudad',
#             'fecha_nacimiento',
#             'direccion',
#             'imagen',
#             'tarjeta_profesional',
#             'especializacion',
#             'consultorio',
#             'password', 
#         ]
#         widgets = {
#             'password': forms.PasswordInput(),
#             'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
#             'imagen':forms.FileInput()
#         }
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['ciudad'].queryset = Ciudad.objects.none()

#             if 'departamento' in self.data:
#                 try:
#                     departamento_id = self.data.get('departamento')
#                     self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento_id=departamento_id)
#                 except:
#                     pass
#             elif self.instance.pk and self.instance.departamento:
#                 self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento=self.instance.departamento)
        
#         def validar_imagen(self):
#             imagen = self.cleaned_data.get(imagen)

#             if imagen:
#                 extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
#                 if extension not in ['jpg', 'png', 'jpeg']:
#                     raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
#                 if imagen.size > 102400:
#                     raise ValidationError('El tamaño máximo del archivo es 100 KB')
#             return imagen

# class AuxAdminFormulario(forms.ModelForm):
#     class Meta:
#         model= AuxAdmin
#         fields=[
#             # 'username', 
#             'first_name', 
#             'last_name', 
#             'email' ,
#             'telefono',
#             'tipo_doc',
#             'documento',
#             'genero',
#             'departamento',
#             'ciudad',
#             'fecha_nacimiento',
#             'direccion',
#             'imagen',
#             'password', 
#         ]
#         widgets = {
#             'password': forms.PasswordInput(),
#             'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
#             'imagen':forms.FileInput()
#         }
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['ciudad'].queryset = Ciudad.objects.none()

#             if 'departamento' in self.data:
#                 try:
#                     departamento_id = self.data.get('departamento')
#                     self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento_id=departamento_id)
#                 except:
#                     pass
#             elif self.instance.pk and self.instance.departamento:
#                 self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento=self.instance.departamento)
#         def validar_imagen(self):
#             imagen = self.cleaned_data.get(imagen)

#             if imagen:
#                 extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
#                 if extension not in ['jpg', 'png', 'jpeg']:
#                     raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
                
#                 if imagen.size > 102400:
#                     raise ValidationError('El tamaño máximo del archivo es 100 KB')
#             return imagen

# class ConsultorioFormulario(forms.ModelForm):
#     class Meta:
#         model= Consultorio
#         fields=[
#             'piso',
#             'num_habitacion',
#         ]

# class CiudadFormulario(forms.ModelForm):
#     class Meta:
#         model= Ciudad
#         fields=[
#             'codigo_municipio',
#             'nombre_ciudad',
#             'codigo_departamento',
#         ]

# class DepartamentoFormulario(forms.ModelForm):
#     class Meta:
#         model=Departamento
#         fields=[
#             'codigo_departamento',
#             'nombre_departamento',
#         ]

# class CitaMedicaFormulario(forms.ModelForm):
#     class Meta:
#         model = CitaMedica
#         fields = ['fecha', 'hora', 'medico', 'paciente', 'lugar']
#         widgets = {
#             'fecha': forms.DateInput(attrs={'type': 'date'}),
#         }
        
# class EspecialidadFormulario(forms.ModelForm):
#     class Meta:
#         model=Especialidad
#         fields=[
#                 'nombre_especialidad',
#                 'descripcion',
#         ]
#         widgets={
#             'descripcion': forms.Textarea(attrs={'rows': 3}),
#         }

# class EstadoCitaFormulario(forms.ModelForm):
#     class Meta:
#         model=EstadoCita
#         fields=[
#             'nombre_estado',
#             'descripcion'
#         ]

# class GrupoIngresosFormulario(forms.ModelForm):
#     class Meta:
#         model=GrupoIngresos
#         fields=[
#             'nivel_ingresos',
#             'valor',
#             'descripcion',
#         ]
        
# class LugarAtencionFormulario(forms.ModelForm):
#     class Meta:
#         model=LugarAtencion
#         fields=[
#             'nombre_lugar',
#             'direccion_lugar',
#             'departamento',
#             'ciudad',
#         ]
#         widgets = {
#             'departamento': forms.Select(attrs={'id': 'id_departamento'}),
#             'ciudad': forms.Select(attrs={'id': 'id_ciudad'}),
#         }
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['ciudad'].queryset = Ciudad.objects.none()

#             if 'departamento' in self.data:
#                 try:
#                     departamento_id = self.data.get('departamento')
#                     self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento_id=departamento_id)
#                 except:
#                     pass
#             elif self.instance.pk and self.instance.departamento:
#                 self.fields['ciudad'].queryset = Ciudad.objects.filter(codigo_departamento=self.instance.departamento)

# class AgendaFormulario(forms.ModelForm):
#     class Meta: 
#         model=Agenda
#         fields=[
#             'medico',
#             'fecha',
#             'hora_inicio',
#             'hora_fin',
#             'fecha_creacion',
#         ]


