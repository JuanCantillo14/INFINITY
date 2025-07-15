from django.db import models
from proyecto_ips_app.models.agenda import Agenda

class SlotCita(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='slots')
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.fecha} - {self.hora_inicio} a {self.hora_fin} ({'Disponible' if self.disponible else 'Ocupado'})"
    class Meta:
        db_table="slot_cita"