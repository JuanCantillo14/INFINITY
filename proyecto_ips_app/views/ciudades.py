from proyecto_ips_app.models import * 
from proyecto_ips_app.forms import *
from django.http import JsonResponse

def cargar_ciudades(request):
    id_departamento = request.GET.get('departamento_id')
    ciudades = Ciudad.objects.filter(codigo_departamento_id=id_departamento).values('codigo_municipio', 'nombre_ciudad')
    return JsonResponse(list(ciudades), safe=False)
