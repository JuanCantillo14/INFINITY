from django.db import models
from proyecto_ips_app.models.usuario import *


class Paciente(Usuario):
    EPS=[('SURA','Sura'),
        ('COMPENSAR','Compensar'),
        ('SANITAS','Sanitas'),
        ('NUEVA EPS','Nueva EPS'),
        ('COOSALUD','Coosalud'),
        ('FAMISANAR','Famisanar')]
    TIPO_REGIMEN=[('CONTR','Contributivo'),
                ('SUB','Subsidiado'),
                ('N/A','No aplica')]
    tipo_regimen=models.CharField(max_length=20,null=False,choices=TIPO_REGIMEN, verbose_name='Tipo de regimen')
    ocupacion=models.CharField(max_length=100,blank=True, verbose_name='Ocupación')
    eps=models.CharField(max_length=20, choices=EPS, null=False)
    
    class Meta:
        db_table='paciente'
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

        
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.is_active = True
            self.rol = 'PAC'
        super().save(*args, **kwargs)
        