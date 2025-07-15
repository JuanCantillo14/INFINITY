from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta
from django.db import models 
from proyecto_ips_app.models.medico import Medico

def validar_dia(value):
    if value < timezone.now().date():
        raise ValidationError("No se puede agendar una fecha en el pasado.")
    if value.weekday() == 6:  # 6 = Domingo
        raise ValidationError("No se pueden agendar citas los domingos.")
    


class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(validators=[validar_dia])
    fecha_fin = models.DateField(validators=[validar_dia], blank= True, null=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    horas_por_dia = models.PositiveSmallIntegerField(default=6)

    class Meta:
        unique_together = ('medico', 'fecha_inicio')
        verbose_name = 'Agenda semanal'
        db_table= 'agenda'

    def clean(self):
        super().clean()

        # Verifica que el inicio sea lunes
        if self.fecha_inicio.weekday() != 0:
            raise ValidationError("La fecha de inicio debe ser un lunes.")
        
        # Calcula automáticamente la fecha de fin como sábado
        self.fecha_fin = self.fecha_inicio + timedelta(days=5)

        # Verifica que la fecha final no incluya domingos
        dia_actual = self.fecha_inicio
        while dia_actual <= self.fecha_fin:
            if dia_actual.weekday() == 6:  # Domingo
                raise ValidationError("No se pueden incluir domingos en la agenda.")
            dia_actual += timedelta(days=1)

        # Verifica solapamiento con otras agendas del mismo médico
        agendas_existentes = Agenda.objects.filter(medico=self.medico).exclude(pk=self.pk)
        for agenda in agendas_existentes:
            if (self.fecha_inicio <= agenda.fecha_fin and self.fecha_fin >= agenda.fecha_inicio):
                raise ValidationError("Ya existe una agenda para este médico en un rango de fechas que se superpone.")
# Validación de horas solo si ambas están definidas
        if self.hora_inicio is None or self.hora_fin is None:
            raise ValidationError("Debe establecer la hora de inicio y fin.")

        hora_valida_1 = (self.hora_inicio.hour == 6 and self.hora_inicio.minute == 0 and
                        self.hora_fin.hour == 12 and self.hora_fin.minute == 0)

        hora_valida_2 = (self.hora_inicio.hour == 12 and self.hora_inicio.minute == 0 and
                        self.hora_fin.hour == 18 and self.hora_fin.minute == 0)

        if not (hora_valida_1 or hora_valida_2):
            raise ValidationError("Solo se permiten turnos de 6:00 a.m. a 12:00 p.m. o de 12:00 p.m. a 6:00 p.m.")

    def save(self, *args, **kwargs):
        if self.fecha_inicio and self.fecha_inicio.weekday() == 0:
            self.fecha_fin = self.fecha_inicio + timedelta(days=5)  # Sábado
        super().save(*args, **kwargs)


    # def duracion_en_horas(self):
    #     inicio_dt = datetime.combine(datetime.today().date(), self.hora_inicio)
    #     fin_dt = datetime.combine(datetime.today().date(), self.hora_fin)
    #     return (fin_dt - inicio_dt).seconds / 3600

    def _str_(self):
        return f'Agenda de {self.medico} desde {self.fecha_inicio}'