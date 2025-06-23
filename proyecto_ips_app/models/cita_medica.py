from django.db import models 
from datetime import date
from django.core.exceptions import ValidationError
from proyecto_ips_app.models.paciente import Paciente
from proyecto_ips_app.models.medico import Medico
from proyecto_ips_app.models.lugar_atencion import LugarAtencion




def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No es posible seleccionar una fecha pasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Seleccione un día hábil de la semana.')


    def __str__(self):
        return f'{self.first_name}'
    
class CitaMedica(models.Model):
    HORA_CHOICES = [(f"{hora:02d}:{minuto:02d}", f"{hora:02d}:{minuto:02d}")
                    for hora in range(7, 15)  # 8 horas desde 7:00 hasta 14:40
                    for minuto in [0, 20, 40]]  # 3 citas por hora

    fecha = models.DateField()
    hora = models.CharField(max_length=5, choices=HORA_CHOICES)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    lugar = models.ForeignKey(LugarAtencion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('realizada', 'Realizada'),
    ], default='pendiente')

    class Meta:
        unique_together = ('fecha', 'hora', 'medico') # Evita duplicar citas
        db_table='cita_medica'

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente.nombre} con {self.medico.nombre}"

    def clean(self):
        super().clean()
        
        citas_en_misma_hora = CitaMedica.objects.filter(
            fecha=self.fecha,
            hora=self.hora,
            medico=self.medico
        )
        if self.pk:
            citas_en_misma_hora = citas_en_misma_hora.exclude(pk=self.pk)

        if citas_en_misma_hora.count() >= 3:
            raise ValidationError(f"Ya hay 3 citas registradas para el médico {self.medico} a las {self.hora} el {self.fecha}.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)