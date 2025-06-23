from django.db import models
from proyecto_ips_app.models.usuario import *
from proyecto_ips_app.models.grupo_ingresos import *

class Paciente(Usuario):
    EPS=[('SURA','Sura'),
        ('COMPENSAR','Compensar'),
        ('SANITAS','Sanitas'),
        ('NUEVA EPS','Nueva EPS'),
        ('COOSALUD','Coosalud'),
        ('FAMISANAR','Famisanar')]
    TIPO_REGIMEN=[('C','Cotizante'),
                ('B','Beneficiario'),
                ('A','Adicional'),
                ('N/A','No aplica')]
    tipo_regimen=models.CharField(max_length=20,null=False,choices=TIPO_REGIMEN, verbose_name='Tipo de regimen')
    ocupacion=models.CharField(max_length=100,blank=True, verbose_name='Ocupación')
    eps=models.CharField(max_length=20, choices=EPS, null=False)
    grupo_ingresos=models.ForeignKey(GrupoIngresos, on_delete=models.SET_NULL, verbose_name='Grupo de Ingresos', null=True)
    
    class Meta:
        db_table='paciente'
        
    def __str__(self):
        return self.first_name, self.last_name

        
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.is_active = True
            self.rol = 'PAC'
        super().save(*args, **kwargs)
        