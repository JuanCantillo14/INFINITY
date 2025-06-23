from rest_framework import viewsets
from proyecto_ips_app.models.usuario import Usuario
from api_app.serializers.usuario import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    
    queryset=Usuario.objects.all()
    serializer_class=UsuarioSerializer