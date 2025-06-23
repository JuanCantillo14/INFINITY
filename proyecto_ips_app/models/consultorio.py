from django.db import models


class Consultorio(models.Model):
    PISO=[('1','1'),
          ('2','2'),
          ('3','3')]
    piso=models.CharField(verbose_name="Piso", null=False, max_length=4, choices=PISO)
    num_habitacion=models.PositiveIntegerField(verbose_name="Número de habitación", null=False)
    
    
    class Meta:
        db_table='consultorio_medico'
        
    def __str__(self):
        return self.num_habitacion
