from django.db import models

class GrupoIngresos(models.Model):
    NIVELINGRESOS=[('A','A'),
                   ('B','B'),
                   ('C','C')]
    nivel_ingresos=models.CharField(choices=NIVELINGRESOS,max_length=5,null=False, verbose_name='Grupo de ingresos')
    valor=models.FloatField(verbose_name='Valor cuota moderadora')
    descripcion=models.CharField(max_length=250, blank=True,verbose_name='Descripción')
    
    class Meta:
        db_table='grupo_ingresos'
    
    def __str__(self):
        return self.nivel_ingresos
    
    