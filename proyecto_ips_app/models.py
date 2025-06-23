# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.exceptions import ValidationError
# from django.core.validators import RegexValidator,MinLengthValidator, MaxLengthValidator,EmailValidator,FileExtensionValidator, MinValueValidator,MaxValueValidator
# from django.utils.translation import gettext_lazy as _
# from django.utils.timezone import now
# import datetime
# import os
# from datetime import date
# from django.conf import settings
# from django.db.models.fields.related import ForeignKey

# # Create your models here.

# #Tipos de Usuarios 

# def user_directory_path(instance, filename):
#     # subcarpeta="img"
#     return f"usuario/img/{instance.id}_{filename}"

# def validar_telefono(value):
#     if len(value)!=10:
#         raise ValidationError(_("%(value)s no es un número telefónico válido"),
#             params={"value": value},
#         )

# def validar_caracter(value):
#     value=RegexValidator
#     value(
#     regex=r'^[A-Za-z\s]+$',
#     message="El campo solo debe contener letras y espacios"
#     )
    
# validar_documento=RegexValidator(
#     regex=r'^\d{4,10}',
#     message="El número de documento no es válido"
# )

# validar_password=RegexValidator(
#     regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{4,}$',
#     message="La contraseña debe tener mínimo 4 caracteres, una mayúscula, un número y un carácter especial"
# )

# #region Usuario 
# class Usuario(AbstractUser):
#     TIPO_DOC=[('CC','Cedula de Ciudadania'),
#             ('CE','Cedula de Extranjeria'),
#             ('TI','Tarjeta de Identidad'),
#             ('RC','Registro Civil')]
#     GENERO=[('M','Masculino'),
#             ('F','Femenino'),
#             ('I','Indefinido')]
#     TIPO_SANGRE=[('A+','A+'),
#                 ('A-','A-'),
#                 ('B+','B+'),
#                 ('B-','B-'),
#                 ('AB+','AB+'),
#                 ('AB-','AB-'),
#                 ('O+','O+'),
#                 ('O-','O-')]
#     ESTADO_CIVIL=[('S','Soltero/a'),
#                 ('C','Casado/a'),
#                 ('V','Viudo/a'),
#                 ('UL','Union libre'),
#                 ('D','Divorciado/a')]
#     first_name=models.CharField(max_length=100,null=False, verbose_name='Nombres',validators=[validar_caracter,MinLengthValidator(3, message="El campo debe contener minimo 3 caracteres")])
#     last_name=models.CharField(max_length=100,null=False, verbose_name='Apellidos',validators=[validar_caracter,MinLengthValidator(5, message="El campo debe contener minimo 5 caracteres")])
#     email=models.EmailField(max_length=100,null=False,unique=True,verbose_name='Correo electrónico',validators=[EmailValidator(message="Correo electrónico inválido")])
#     documento=models.IntegerField(unique=True, null=False,verbose_name='Número de documento',validators=[validar_documento])
#     tipo_doc=models.CharField(choices=TIPO_DOC,max_length=2, verbose_name='Tipo de documento', default='CC')
#     genero=models.CharField(max_length=1,null=False,choices=GENERO, verbose_name='Genero',default='M')
#     tipo_sangre=models.CharField(max_length=3,null=False,choices=TIPO_SANGRE, verbose_name='Tipo de sangre',default='O+')
#     fecha_nacimiento=models.DateField(null=False, verbose_name='Fecha de nacimiento',validators=[MaxValueValidator(datetime.date.today)],default=now)
#     telefono=models.CharField(max_length=10,null=False, verbose_name='Número de telefono', validators=[validar_telefono],unique=True,default='300437243')
#     ciudad=models.CharField(max_length=100, null=False,verbose_name='Ciudad de residencia',validators=[validar_caracter],default='Soacha')
#     direccion=models.CharField(max_length=100,null=False, verbose_name='Dirección de residencia',default='Calle 23 A SUR')
#     eps=models.CharField(max_length=100,blank=True, verbose_name='EPS',default='SURA')
#     estado_civil=models.CharField(max_length=20,null=False,choices=ESTADO_CIVIL, verbose_name='Estado civil',default='C')
#     imagen=models.ImageField(upload_to=user_directory_path,blank=True, null=True, verbose_name='Imagen de Usuario',validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])]) #IMAGEEEEEEEEEEEEN
#     password=models.CharField(max_length=100, null=False, verbose_name='Contraseña')#, validators=[validar_password])
#     #arl 

#     @property 
#     def medico(self):
#         return isinstance(self,Medico)

#     @property
#     def aux_admin(self):
#         return isinstance(self,AuxAdmin)
    
#     @property
#     def paciente(self):
#         return isinstance(self,Paciente)
    
#     def delete(self,*args,**kwards): # Numero indefinido de argumentos **
#         if self.imagen:
#             imagen_path=self.imagen.path
#             if os.path.exists(imagen_path):
#                 os.remove(imagen_path)
#         super().delete(*args,**kwards)
    
#     def save(self,*args,**kwards):
#         if not self.username: 
#             self.username=self.documento
#         if self.id:
#             usuario_antiguo=Usuario.objects.filter(id=self.id).get()
#             if usuario_antiguo and usuario_antiguo.imagen:
#                 imagen_anterior=usuario_antiguo.imagen.path
#                 if self.imagen!=usuario_antiguo.imagen:
#                     if os.path.exists(imagen_anterior):
#                         os.remove(imagen_anterior)
#         super().save(*args,**kwards)
# #endregion

# #region Administrador    

# class Administrador(Usuario):
#     codigo = models.CharField(max_length=20)
#     fecha_ingreso = models.DateField()

#     def habilitar_usuario(self, usuario):
#         usuario.is_active = True
#         usuario.save()

#     def inhabilitar_usuario(self, usuario):
#         usuario.is_active = True
#         usuario.save()

# #endregion 

# #region Paciente

# class Paciente(Usuario):
#     TIPO_POBLACION=[('N/A','Ninguna'),
#                     ('PIV','Poblacion Infantil vulnerable'),
#                     ('AMV','Adulto mayor vulnerable'),
#                     ('M','Migrante'),
#                     ('PD','Población desmovilizada'),
#                     ('CI','Comunidad indigena'),
#                     ('VFP','Veterano fuerza pública')]
#     TIPO_REGIMEN=[('C','Cotizante'),
#                 ('B','Beneficiario'),
#                 ('A','Adicional'),
#                 ('N/A','No aplica')]
#     ESTRATO_SOCIAL=[('E1','Estrato 1'),
#                     ('E2','Estrato 2'),
#                     ('E3','Estrato 3'),
#                     ('E4','Estrato 4'),
#                     ('E5','Estrato 5'),
#                     ('E6','Estrato 6')]
#     tipo_poblacion=models.CharField(max_length=100,null=False,choices=TIPO_POBLACION, verbose_name='Tipo de población',default='N/A')
#     tipo_regimen=models.CharField(max_length=20,null=False,choices=TIPO_REGIMEN, verbose_name='Tipo de regimen')
#     estrato_social=models.CharField(max_length=20,null=False, choices=ESTRATO_SOCIAL, verbose_name='Estrato social')
#     ocupacion=models.CharField(max_length=100,blank=True, verbose_name='Ocupación')
#     TIPO_PACIENTE = [
#         ('ESTANDAR', 'Estandar'),
#         ('PREMIUM', 'Premium')
#         ]
#     tipo_paciente = models.CharField(max_length=10, choices=TIPO_PACIENTE, default='ESTANDAR',verbose_name='Tipo de paciente')
    
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# #endregion 

# #region Empleado
# class Empleado(Usuario):
#     fecha_ing=models.DateField(null=False, default=now, verbose_name='Fecha de ingreso')
    
#     def __str__(self):
#         return self.first_name

# #endregion 

# #region Especialidad
# class Especialidad(models.Model):
#     codigo_especialidad=models.CharField(max_length=50, verbose_name='Especialidad',unique=True)
#     nombre = models.CharField(verbose_name="Nombre", max_length=200)
#     descripcion=models.TextField(verbose_name="Descripcion de la especialidad ")
    
    
#     def __str__(self):
#         return f'{self.nombre}'
# #endregion

# #region Medico
# class Medico(Empleado):
#     tarjeta_prof=models.CharField(max_length=15, null=False, unique=True, db_index=True, verbose_name='Número de tarjeta profesional')
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="El número debe estar en este formato: '+99 99 9999-0000'.")
#     especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name='medicos')
   
   
#     def __str__(self):
#         return f'{self.nombre}'

# #endregion 

# #region AuxAdmin
# class AuxAdmin(Empleado):
#     departamento_trabajo=models.CharField(max_length=100, blank=True,verbose_name='Departamento de trabajo')
    
#     def __str__(self):
#         return self.first_name

# #endregion 
    

# #region Diagnostico
# class Diagnostico(models.Model):
#     codigo_enfermedad=models.TextField(blank=True, verbose_name='Codigo del diagnóstico')
#     nombre_enfermedad=models.TextField(blank=True, verbose_name='Nombre de la enfermedad')
#     descr_enfermedad=models.TextField(blank=True, verbose_name='Descripción de la enfermedad')
    
    
# #endregion 
    
# #region Vacunas    
# class Vacunas(models.Model):
#     descripcion=models.TextField()
#     dosis=models.CharField(max_length=100)
#     fecha_vac=models.DateField()
#     nro_dosis=models.CharField(max_length=50)
#     refuerzos=models.CharField(max_length=100)
#     via_aplicacion=models.CharField(max_length=100)
#     eventos_adversos=models.TextField()
#     intervalo=models.CharField(max_length=100)
    
# #endregion

# #region Antecedentes

# class Antecedentes(models.Model):
#     patologicos=models.TextField(verbose_name='Antecedentes patológicos')
#     quirurgicos=models.TextField(verbose_name='Antecedentes quirurgicos')
#     alergicos=models.TextField(verbose_name='Antecedentes alergicos')
#     ginecologicos=models.TextField(verbose_name='Antecedentes ginecológicos')
#     obstetricos=models.TextField(verbose_name='Antecedentes obstetricos')
#     farmacologicos=models.TextField(verbose_name='Antecedentes farmacológicos')
#     familiares=models.TextField(verbose_name='Antecedentes familiares')
# #endregion


# #region FormulaMedica
# class FormulaMedica(models.Model):
#     VIA_ADMON=[('ENTERAL','Enteral'),
#             ('PARENTAL','Parental'),
#             ('TÓPICA','Tópica'),
#             ('TRANSD','Transdérmica')]
#     medicamento=models.CharField(max_length=100, null=False, verbose_name='Medicamento remitido')
#     dosificacion=models.CharField(max_length=100, null=False, verbose_name='Dosificación del medicamento')
#     via_admon=models.CharField(max_length=20,choices=VIA_ADMON,null=False, verbose_name='Via de Administración')
#     cantidad=models.CharField(max_length=50,null=False, verbose_name='Cantidad')
#     recomendacion=models.TextField(blank=True, verbose_name='Recomendaciones')
#     punto_entrega=models.CharField(max_length=200, null=False, verbose_name='Punto de entrega')
#     tipo_convenio=models.CharField(max_length=10, blank=True, verbose_name='Tipo de convenio')
#     dato_contacto=models.CharField(max_length=10, null=False, verbose_name='Datos de contacto')
#     fecha_exp=models.DateTimeField(null=False, default=datetime.date.today, verbose_name='Fecha de expedición de la orden médica')

# #endregion

# #region SignosVitales
# class SignosVitales(models.Model):
#     descripcion=models.TextField(blank=True, verbose_name='Descripción general')
#     peso=models.PositiveSmallIntegerField(null=False, verbose_name='Peso(kg)')
#     talla=models.PositiveSmallIntegerField(null=False, verbose_name='Talla(cm)')
#     respiracion=models.CharField(max_length=5, null=False, verbose_name='Respiración')
#     pulso=models.CharField(max_length=5, null=False, verbose_name='Pulso')
#     temperatura=models.FloatField(null=False, verbose_name='Temperatura(°C)',validators=[MinValueValidator(35.0),MaxValueValidator(39.0)])
# #endregion

# #region Agenda(HORARIO)

# def validar_dia(value):
#     today = date.today()
#     weekday = date.fromisoformat(f'{value}').weekday()

#     if value < today:
#         raise ValidationError('No es posible seleccionar una fecha pasada.')
#     if (weekday == 5) or (weekday == 6):
#         raise ValidationError('Seleccione un día hábil de la semana.')


#     def __str__(self):
#         return f'{self.first_name}'
    
# class CitaMedica(models.Model):
#     medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda')
#     dia = models.DateField(help_text="Seleccione una fecha para la agenda", validators=[validar_dia])
   
#     HORARIOS = (
#         ("1", "07:00 a 08:00"),
#         ("2", "08:00 a 09:00"),
#         ("3", "09:00 a 10:00"),
#         ("4", "10:00 a 11:00"),
#         ("5", "11:00 a 12:00"),
#     )
#     horario = models.CharField(max_length=10, choices=HORARIOS,null=False)
   
#     paciente = models.ForeignKey(Paciente,verbose_name='Usuario',on_delete=models.CASCADE)
   
#     class Meta:
#         unique_together = ('horario', 'dia')
       
#     def __str__(self):
#         return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.medico}'
    
    
# #region Examen Fisico
# class ExamenFisico(models.Model):
#     cita = models.ForeignKey(CitaMedica, on_delete=models.CASCADE)
#     cod_remision=models.CharField(null=False,max_length=20, verbose_name='Código de remisión')
#     cabeza_cuello_otros=models.TextField(blank=True, verbose_name='Cabeza, cuello, otras consideraciones')
#     cardiorespiratorio=models.TextField(blank=True, verbose_name='Cardiorespiratorio')
#     gastrointestinal=models.TextField(blank=True, verbose_name='Gastrointestinal')
#     genito_urinario=models.TextField(blank=True, verbose_name='Genito Urinario')
#     osteomuscular=models.TextField(blank=True, verbose_name='Osteomuscular')
#     extremidad_inferior=models.TextField(blank=True, verbose_name='Extremidades inferiores')
#     neurologico=models.TextField(blank=True, verbose_name='Consideraciones neurológicas')
#     hematopoyetico=models.TextField(blank=True, verbose_name='Hematopoyetico')
#     piel_farenas=models.TextField(blank=True, verbose_name='Piel, farenas')
#     otros=models.TextField(blank=True, verbose_name='Otras consideraciones')
    
#     def __str__(self):
#         return f"Examen Físico de {self.cita}"

# #endregion
