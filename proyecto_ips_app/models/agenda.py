from django.db import models 
from proyecto_ips_app.models.medico import Medico
from datetime import date
from django.core.exceptions import ValidationError


def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No es posible seleccionar una fecha pasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Seleccione un día hábil de la semana.')
    
class Agenda(models.Model): 
    medico=models.ForeignKey(Medico, verbose_name='Agenda Médica', on_delete=models.CASCADE)
    fecha=models.DateField(help_text="Seleccione una fecha para la agenda",validators=[validar_dia], null=False)
    HORARIOS = (
        ("1", "07:00 a 08:00"),
        ("2", "08:00 a 09:00"),
        ("3", "09:00 a 10:00"),
        ("4", "10:00 a 11:00"),
        ("5", "11:00 a 12:00"),
    )
    hora_inicio=models.TimeField(help_text="Seleccione un horario",null=False)
    hora_fin=models.TimeField(help_text="Seleccione un horario",null=False)
    fecha_creacion=models.DateTimeField()
    
    class Meta:
        db_table='agenda'
