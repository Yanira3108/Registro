from rest_framework.serializers import ModelSerializer
from apps.registro.models import Registro

class RegisSerializer(ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'
        
    def create(self, validate_data):
        return Registro.objects.create(**validate_data)