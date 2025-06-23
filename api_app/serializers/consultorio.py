from rest_framework import serializers
from proyecto_ips_app.models.consultorio import Consultorio

class ConsultorioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Consultorio
        fields='__all__'