from rest_framework.viewsets import ViewSet
from rest_framework. response import Response
from rest_framework import status
from apps.registro.models import Registro
from apps.registro.api.serializers import RegisSerializer

# Create your views here.
class RegApiView(ViewSet):
    def list(self, request):
        serializer= RegisSerializer(Registro.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self,request, pk=int):
        serializer = RegisSerializer(Registro.object.get(pk=int))
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
    def create(self, request):
        serializer = RegisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
