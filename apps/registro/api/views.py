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
        serializer = RegisSerializer(Registro.objects.get(pk=int))
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
    def create(self, request):
        serializer = RegisSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
    def update(self, request, pk=None):
        try:
            Registro = Registro.objects.get(pk=pk)
        except Registro.DoesNotExist:
            return Response({'error': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RegisSerializer(Registro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            producto = Registro.objects.get(pk=pk)
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Registro.DoesNotExist:
            return Response({'error': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
