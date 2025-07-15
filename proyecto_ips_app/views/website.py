from django.shortcuts import render

from proyecto_ips_app.models import *
from proyecto_ips_app.forms import *

def website(request):
    return render(request, 'website/website.html')