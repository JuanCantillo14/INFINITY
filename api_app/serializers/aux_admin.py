from rest_framework import serializers
from proyecto_ips_app.models.aux_admin import AuxAdmin

class AuxAdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= AuxAdmin
        fields='__all__'