from django.db import models

class EstadoCita(models.Model):
    ESTADOCITA=[('PROGRAMADA','Programada'),('CANCELADA','Cancelada'),('FINALIZADA','Finalizada')]
    nombre_estado=models.CharField(choices=ESTADOCITA, max_length=20, null=False, verbose_name='Estado de la Cita')
    descripcion=models.CharField(max_length=255, blank=True)
    
    class Meta:
        db_table='estado_cita'
    def __str__(self):
        return self.nombre_estado
    
 