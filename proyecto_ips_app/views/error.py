from django.shortcuts import render
from django.http import HttpResponseNotFound

def error_404(request):
    return render(request, 'error/404.html', status=404)

def error_400(request):
    return render(request, '400.html', status=400)

def error_403(request):
    return render(request, '403.html', status=403)

def error_500(request):
    return render(request, '500.html', status=500)

