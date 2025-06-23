from django.db import models

class Departamento(models.Model):
    codigo_departamento=models.CharField(max_length=10, null=False, verbose_name='Código del departamento', unique=True, primary_key=True)
    nombre_departamento=models.CharField(max_length=255, null=False, verbose_name='Nombre del departamento', unique=True)
    
    class Meta:
        db_table='departamento'
        
    def __str__(self):
        return self.nombre_departamento
    