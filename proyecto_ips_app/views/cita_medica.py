from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *

def agendar_cita(request):
    if request.method == 'POST':
        form = CitaMedicaFormulario(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Cita agendada con éxito.")
                return redirect('agendar_cita')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = CitaMedicaFormulario()
    
    return render(request, 'agendar_cita.html', {'form': form})

def actualizar_cita(request, id):
    cita = get_object_or_404(CitaMedica, id=id)

    if request.method == "POST":
        form_cita = CitaMedicaFormulario(request.POST, instance=cita)

        if form_cita.is_valid():
            # Guardamos la cita actualizada
            cita = form_cita.save()

            messages.success(request, 'Cita actualizada y formularios creados exitosamente.')
            return redirect('detallar_cita', id=id)
        else:
            messages.error(request, 'Hay errores en los formularios. Verifica los datos.')

    else:
        form_cita = CitaMedicaFormulario(instance=cita)


    return render(request, 'cita/actualizar.html', {
        'form_cita': form_cita,
        'cita': cita  # por si lo necesitás en el template
    })

# def detallar_cita(request,id):
#     citas = get_object_or_404(CitaMedica, id=id)
#     return render(request, 'cita/detallar.html', {
#         'citas': citas
#     })
def detallar_cita(request, id):
    cita = get_object_or_404(CitaMedica, id=id)
    return render(request, 'cita/detallar.html', {'citas': [cita]})



def listar_citas(request):
    citas = CitaMedica.objects.all()
    return render(request, 'cita/listar.html', {'citas':citas})
