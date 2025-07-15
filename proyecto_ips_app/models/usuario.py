from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator,MinLengthValidator, MaxLengthValidator,EmailValidator,FileExtensionValidator, MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now 
import datetime
import os
from proyecto_ips_app.models.ciudad import *
from proyecto_ips_app.models.departamento import *

# Create your models here.

#Tipos de Usuarios 

def user_directory_path(instance, filename):
    # subcarpeta="img"
    return f"usuario/img/{instance.id}_{filename}"

def validar_telefono(value):
    if len(value)!=10:
        raise ValidationError(_("%(value)s no es un número telefónico válido"),
            params={"value": value},
        )

def validar_caracter(value):
    value=RegexValidator
    value(
    regex=r'^[A-Za-z\s]+$',
    message="El campo solo debe contener letras y espacios"
    )
    
validar_documento=RegexValidator(
    regex=r'^\d{4,10}',
    message="El número de documento no es válido"
)

validar_password=RegexValidator(
    regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{4,}$',
    message="La contraseña debe tener mínimo 4 caracteres, una mayúscula, un número y un carácter especial"
)

#region Usuario 
class Usuario(AbstractUser):
    TIPO_DOC=[('CC','Cedula de Ciudadania'),
            ('CE','Cedula de Extranjeria'),
            ('TI','Tarjeta de Identidad'),
            ('RC','Registro Civil')]
    GENERO=[('M','Masculino'),
            ('F','Femenino'),
            ('I','Indefinido')]
    ROL=[
        ('MED','Medico'),
        ('PAC','Paciente'),
        ('AUX','AuxAdministrativo'),
    ]
    username = models.CharField(
        max_length=150, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',  # Solo permite letras, dígitos y los caracteres permitidos
                message="El campo username solo puede contener letras, números y los caracteres @/./+/-/_"
            ),
        ],
        verbose_name="Username"
    )
    rol = models.CharField(max_length=20, choices=ROL, default='PAC', verbose_name='Rol en la empresa')
    first_name=models.CharField(max_length=100,null=False, verbose_name='Nombres',validators=[validar_caracter,MinLengthValidator(3, message="El campo debe contener minimo 3 caracteres")])
    last_name=models.CharField(max_length=100,null=False, verbose_name='Apellidos',validators=[validar_caracter,MinLengthValidator(5, message="El campo debe contener minimo 5 caracteres")])
    email=models.EmailField(max_length=100,null=False,unique=True,verbose_name='Correo electrónico',validators=[EmailValidator(message="Correo electrónico inválido")])
    telefono=models.CharField(max_length=10,null=False, verbose_name='Número de telefono',default='300437243',validators=[validar_telefono])
    tipo_doc=models.CharField(choices=TIPO_DOC,max_length=2, verbose_name='Tipo de documento', default='CC')
    documento=models.CharField(unique=True, max_length=10, null=False,verbose_name='Número de documento',validators=[validar_documento])
    genero=models.CharField(max_length=1,null=False,choices=GENERO, verbose_name='Genero',default='M')
    departamento=models.ForeignKey(Departamento, max_length=100, blank=True,verbose_name='Departamento de residencia', on_delete=models.SET_NULL, null=True)
    ciudad=models.ForeignKey(Ciudad, max_length=100, blank=True,verbose_name='Ciudad de residencia', on_delete=models.SET_NULL, null=True)
    fecha_nacimiento=models.DateField(null=False, verbose_name='Fecha de nacimiento',validators=[MaxValueValidator(datetime.date.today)],default=now)
    direccion=models.CharField(max_length=100,null=False, verbose_name='Dirección de residencia',default='Calle 23 A SUR')
    imagen=models.ImageField(upload_to=user_directory_path,blank=True, null=True, verbose_name='Imagen de Usuario',validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])]) #IMAGEEEEEEEEEEEEN
    password=models.CharField(max_length=100, null=False, verbose_name='Contraseña')#, validators=[validar_password])
    #arl 
    
    class Meta:
        db_table='usuarios'
        
    def delete(self,*args,**kwards): # Numero indefinido de argumentos **
        if self.imagen:
            imagen_path=self.imagen.path
            if os.path.exists(imagen_path):
                os.remove(imagen_path)
        super().delete(*args,**kwards)
    
    def save(self,*args,**kwards):
        if not self.username: 
            self.username=self.documento
        if self.id:
            usuario_antiguo=Usuario.objects.filter(id=self.id).get()
            if usuario_antiguo and usuario_antiguo.imagen:
                imagen_anterior=usuario_antiguo.imagen.path
                if self.imagen!=usuario_antiguo.imagen:
                    if os.path.exists(imagen_anterior):
                        os.remove(imagen_anterior)
        super().save(*args,**kwards)
        
    groups = models.ManyToManyField(
        Group,
        related_name="usuario_set",  # Cambia el nombre para evitar conflictos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuario_permisos_set",  # Cambia el nombre para evitar conflictos
        blank=True
    )
    def user_directory_path(instance, filename):
        return f'usuarios/{instance.username}/{filename}'

    
