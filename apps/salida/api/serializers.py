from rest_framework.serializers import ModelSerializer
from apps.salida.models import Salida

class SalirSerializer(ModelSerializer):
    class Meta:
        model = Salida
        fields = '__all__'
        
