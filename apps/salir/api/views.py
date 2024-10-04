from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.salir.models import Salir
from apps.salir.api.serializers import SalirSerializers

# Create your views here.
class SalirApiView(APIView):
    def get(self, request): 
        data = Salir.objects.all()
