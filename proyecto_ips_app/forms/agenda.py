from django import forms
from proyecto_ips_app.models.agenda import Agenda
from datetime import time

class AgendaForm(forms.ModelForm):
    HORARIO_CHOICES = [
        ('diurna', 'Diurna (6:00am - 12:00pm)'),
        ('tarde', 'Tarde (12:00pm - 6:00pm)'),
    ]

    horario = forms.ChoiceField(
        choices=HORARIO_CHOICES,
        widget=forms.RadioSelect,
        label="Horario"
    )

    class Meta:
        model = Agenda
        fields = ['medico', 'fecha_inicio', 'horas_por_dia', 'horario']

    def clean(self):
        cleaned_data = super().clean()
        horario = cleaned_data.get('horario')

        if horario == 'diurna':
            self.instance.hora_inicio = time(6, 0)
            self.instance.hora_fin = time(12, 0)
        elif horario == 'tarde':
            self.instance.hora_inicio = time(12, 0)
            self.instance.hora_fin = time(18, 0)
        else:
            raise forms.ValidationError("Debe seleccionar un horario válido.")

        return cleaned_data