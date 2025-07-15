from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import json

from proyecto_ips_app.models.medico import Medico
from proyecto_ips_app.models.agenda import Agenda
from proyecto_ips_app.models.cita_medica import Cita
from proyecto_ips_app.models.lugar_atencion import LugarAtencion
from proyecto_ips_app.models.paciente import Paciente


# VISTA 1: Mostrar calendario, fechas y horas disponibles
@login_required
def agendar_cita(request):
    medicos = Medico.objects.all()
    medico_id = request.GET.get('medico')
    fecha_seleccionada = request.GET.get('fecha')

    citas_disponibles = []
    fechas_disponibles = []

    if medico_id:
        medico = Medico.objects.get(pk=medico_id)
        agendas = Agenda.objects.filter(medico=medico)

        # Construir lista de fechas disponibles
        for agenda in agendas:
            actual = agenda.fecha_inicio
            while actual <= agenda.fecha_fin:
                fechas_disponibles.append(actual.strftime("%Y-%m-%d"))
                actual += timedelta(days=1)

        if fecha_seleccionada:
            fecha_obj = datetime.strptime(fecha_seleccionada, "%Y-%m-%d").date()
            agenda_del_dia = Agenda.objects.filter(
                medico=medico,
                fecha_inicio__lte=fecha_obj,
                fecha_fin__gte=fecha_obj
            ).first()

            if agenda_del_dia:
                citas_ocupadas = Cita.objects.filter(
                    medico=medico,
                    fecha=fecha_obj
                ).values_list('hora', flat=True)

                hora_inicio = agenda_del_dia.hora_inicio
                hora_fin = agenda_del_dia.hora_fin

                hora_actual_dt = datetime.combine(datetime.today(), hora_inicio)
                hora_fin_dt = datetime.combine(datetime.today(), hora_fin)

                while hora_actual_dt < hora_fin_dt:
                    hora_disponible = hora_actual_dt.time()
                    if hora_disponible not in citas_ocupadas:
                        citas_disponibles.append(hora_disponible)
                    hora_actual_dt += timedelta(minutes=20)

    # Convertimos fechas a JSON para el calendario JS
    fechas_json = json.dumps(fechas_disponibles)
    lugares = LugarAtencion.objects.all()

    # Obtener lista de pacientes solo si el usuario es auxiliar
    pacientes = Paciente.objects.filter(is_active=True) if hasattr(request.user, 'auxadmin') else None

    return render(request, 'cita/agendar_cita.html', {
        'medicos': medicos,
        'fechas_disponibles': fechas_disponibles,
        'fechas_json': fechas_json,
        'citas_disponibles': citas_disponibles,
        'fecha_seleccionada': fecha_seleccionada,
        'medico_id': medico_id,
        'lugares': lugares,
        'pacientes': pacientes,
    })


# VISTA 2: Crear cita médica
@login_required
def crear_cita(request):
    if request.method == 'POST':
        medico_id = request.POST.get('medico_id')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        lugar = LugarAtencion.objects.first()  # Puedes ajustarlo si tienes lógica para múltiples lugares

        # Si el que agenda es auxiliar, se selecciona el paciente desde el formulario
        if hasattr(request.user, 'auxadmin'):
            paciente_id = request.POST.get('paciente_id')
            if not paciente_id:
                messages.error(request, "Debes seleccionar un paciente.")
                return redirect(f'/cita/agendar/?medico={medico_id}&fecha={fecha}')
            try:
                paciente = Paciente.objects.get(id=paciente_id)
            except Paciente.DoesNotExist:
                messages.error(request, "Paciente no encontrado.")
                return redirect(f'/cita/agendar/?medico={medico_id}&fecha={fecha}')
        else:
            paciente = request.user

        # Validaciones
        if Cita.objects.filter(medico_id=medico_id, fecha=fecha, hora=hora).exists():
            messages.error(request, "La hora ya fue reservada.")
            return redirect(f'/cita/agendar/?medico={medico_id}&fecha={fecha}')

        if Cita.objects.filter(paciente=paciente, medico_id=medico_id, fecha=fecha).exists():
            
            messages.error(request, "Este paciente ya tiene una cita con este médico ese día.")
            return redirect(f'/cita/agendar/?medico={medico_id}&fecha={fecha}')

        # Crear la cita
        Cita.objects.create(
            medico_id=medico_id,
            paciente=paciente,
            lugar_atencion=lugar,
            fecha=fecha,
            hora=hora,
            estado='PENDIENTE'
        )
        messages.success(request, "Cita agendada correctamente.")
        if hasattr(request.user, 'auxadmin'):
            return redirect('agendar_cita')  # O a donde desees redirigir al auxiliar
        else:
            return redirect('mis_citas')

    return redirect('agendar_cita')

# Vista de paciente - citas propias
@login_required
def mis_citas(request):
    citas = Cita.objects.filter(paciente=request.user).order_by('fecha', 'hora')
    return render(request, 'cita/mis_citas.html', {'citas': citas})


# Vista del médico - sus citas
@login_required
def citas_medico(request):
    medico = getattr(request.user, 'medico', None)
    if not medico:
        messages.error(request, "No tienes permisos para ver esta página.")
        return redirect('inicio')  # Cambia a la ruta deseada

    citas = Cita.objects.filter(medico=medico).order_by('fecha', 'hora')
    return render(request, 'medico/citas_medico.html', {'citas': citas})

@login_required
def cancelar_cita(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)

    # Solo puede cancelar si es el paciente dueño o un auxiliar
    if cita.paciente == request.user or hasattr(request.user, 'auxadmin'):
        cita.estado = 'CANCELADA'
        cita.save()
        messages.success(request, "La cita fue cancelada correctamente.")
    else:
        messages.error(request, "No tienes permisos para cancelar esta cita.")

    return redirect('mis_citas' if hasattr(request.user, 'paciente') else 'agendar_cita')

from django.db.models import Q

@login_required
def citas_auxiliar(request):
    # Verifica si el usuario es un auxiliar administrativo
    if not hasattr(request.user, 'auxadmin'):
        messages.error(request, "No tienes permisos para ver esta página.")
        return redirect('inicio')  # Cambia a tu vista principal

    consultaSQL = request.GET.get('consultaSQL', '').strip()
    citas = Cita.objects.select_related('paciente', 'medico', 'lugar_atencion')

    if consultaSQL:
        citas = citas.filter(
            Q(paciente__first_name__icontains=consultaSQL) |
            Q(paciente__last_name__icontains=consultaSQL) |
            Q(medico__first_name__icontains=consultaSQL) |
            Q(medico__last_name__icontains=consultaSQL)
        )

        if not citas.exists():
            messages.info(request, "No se encontraron citas con ese criterio.")

    citas = citas.order_by('-fecha', '-hora')

    return render(request, 'aux_admin/citas_auxiliar.html', {
        'citas': citas,
        'consultaSQL': consultaSQL
    })
