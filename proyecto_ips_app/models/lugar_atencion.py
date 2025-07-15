from django.db import models
from proyecto_ips_app.models.ciudad import *
from proyecto_ips_app.models.departamento import *

class LugarAtencion(models.Model):
    nombre_lugar = models.CharField(max_length=255, verbose_name="Lugar de Atención", null=False, unique=True)
    direccion_lugar = models.CharField(max_length=255, null=False, verbose_name="Dirección del lugar de atención")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table='lugar_atencion'

    def __str__(self):
        return f"{self.nombre_lugar} {self.direccion_lugar}"