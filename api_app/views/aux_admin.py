from rest_framework import viewsets
from proyecto_ips_app.models.aux_admin import AuxAdmin
from api_app.serializers.aux_admin import AuxAdminSerializer

class AuxAdminViewSet(viewsets.ModelViewSet):
    
    queryset=AuxAdmin.objects.all()
    serializer_class=AuxAdminSerializer