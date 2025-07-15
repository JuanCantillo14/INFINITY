# models/cita.py
from django.db import models
from proyecto_ips_app.models.medico import Medico
from proyecto_ips_app.models.usuario import Usuario
from proyecto_ips_app.models.lugar_atencion import LugarAtencion  # Asegúrate de tenerlo
from django.utils import timezone

ESTADO_CITA = [
    ('PENDIENTE', 'Pendiente'),
    ('CONFIRMADA', 'Confirmada'),
    ('CANCELADA', 'Cancelada'),
    ('ATENDIDA', 'Atendida'),
]

class Cita(models.Model):
    medico = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='citas_como_medico'
    )
    paciente = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name='citas_como_paciente'
    )
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_CITA, default='PENDIENTE')
    lugar_atencion = models.ForeignKey(LugarAtencion, null=True, blank=True, default="Asistir Salud LTDA",on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('medico', 'fecha', 'hora')  # No se puede agendar más de una cita en la misma hora
        db_table="cita"