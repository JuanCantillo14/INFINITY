from django.db import models

class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=200, null=False, verbose_name='Nombre de la especialidad')
    descripcion = models.TextField(null=False, verbose_name='Descripción de la especialidad')
    
    class Meta:
        db_table='especialidad'
    
    def __str__(self):
        return f"{self.nombre_especialidad}"
    
  