from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.salida.models import Salida
from apps.salida.api.serializers import SalirSerializer

# Create your views here.
class SalirViewSet(ViewSet):
    
    def list(self, request):
        serializer= SalirSerializer(Salida.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self,request, pk=int):
        serializer = SalirSerializer(Salida.objects.get(pk=pk))
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
    def create(self, request):
        serializer = SalirSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)

    def update(self, request, pk=int):
        try:
            salida = Salida.objects.get(pk=pk)
        except salida.DoesNotExist:
            return Response({'error': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SalirSerializer(salida, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=int):
        try:
            producto = Salida.objects.get(pk=pk)  # Buscar el producto por ID
        except Salida.DoesNotExist:
            return Response({'error': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SalirSerializer(producto, data=request.data, partial=True)  # Permitir actualización parcial
        if serializer.is_valid():
            serializer.save()  # Guardar los cambios
            return Response(serializer.data)  # Devolver los datos actualizados
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=int):
        try:
            producto = Salida.objects.get(pk=pk)
            producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Salida.DoesNotExist:
            return Response({'error': 'Producto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
  
