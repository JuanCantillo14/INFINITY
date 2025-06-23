from django.db import models
from proyecto_ips_app.models.ciudad import *
from proyecto_ips_app.models.departamento import *

class LugarAtencion(models.Model):
    nombre_lugar = models.CharField(max_length=255, verbose_name="Lugar de Atención", null=False)
    direccion_lugar = models.CharField(max_length=255, null=False, verbose_name="Dirección del lugar de atención")
    departamento=models.ForeignKey(Departamento, on_delete=models.SET_NULL, verbose_name="Departamento", max_length=200, null=True)
    ciudad=models.ForeignKey(Ciudad, on_delete=models.SET_NULL,verbose_name="Ciudad", max_length=200, null=True)
    
    class Meta:
        db_table='lugar_atencion'