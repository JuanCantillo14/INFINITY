from django.db import models
from proyecto_ips_app.models.usuario import *
from proyecto_ips_app.models.especialidad import *

class Medico(Usuario):
    tarjeta_profesional=models.CharField(max_length=15, null=False, unique=True, db_index=True, verbose_name='Número de tarjeta profesional')
    especializacion=models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, verbose_name='Especialidad')

    class Meta:
        db_table='medico'
        
    def __str__(self):
        return f"{self.first_name} {self. last_name}"
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.is_active = True
            self.rol = 'MED'
        super().save(*args, **kwargs)
        
    
