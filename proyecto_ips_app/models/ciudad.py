from django.db import models 
from proyecto_ips_app.models.departamento import *

class Ciudad(models.Model):
    codigo_municipio=models.CharField(max_length=10, null=False, unique=True, verbose_name="Código del Municipio", primary_key=True)
    nombre_ciudad=models.CharField(max_length=255, null=False, verbose_name="Nombre de la Ciudad")
    codigo_departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento", max_length=200)
    
    class Meta:
        db_table='ciudad'
        
    def __str__(self):
        return self.nombre_ciudad
    
 