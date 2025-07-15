from django.shortcuts import render, redirect
from proyecto_ips_app.forms.agenda import AgendaForm
from proyecto_ips_app.models.agenda import Agenda
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def crear_agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            try:
                agenda = form.save()  # ahora se asignan las horas antes del clean() del modelo
                return redirect('listar_agenda')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = AgendaForm()
    return render(request, 'agenda/crear_agenda.html', {'form': form})


def listar_agenda(request):
    agendas = Agenda.objects.select_related('medico').all()
    return render(request, 'agenda/listar_agenda.html', {'agendas': agendas})

from collections import defaultdict

@login_required
def listar_agenda_aux(request):
    consultaSQL = request.GET.get('consultaSQL', '').strip()
    agendas = []

    if consultaSQL:
        # Filtra por nombre, apellido o documento del médico
        agendas = Agenda.objects.select_related('medico').filter(
            Q(medico__first_name__icontains=consultaSQL) |
            Q(medico__last_name__icontains=consultaSQL) |
            Q(medico__documento__icontains=consultaSQL)
        ).order_by('medico__first_name', 'fecha_inicio')

        if not agendas.exists():
            messages.info(request, "No se encontraron agendas para ese médico.")

    agendas_por_medico = defaultdict(list)
    for agenda in agendas:
        agendas_por_medico[agenda.medico].append(agenda)

    return render(request, 'agenda/listar_agenda_aux.html', {
        'agendas_por_medico': agendas_por_medico.items(),
        'consultaSQL': consultaSQL
    })