from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


from .models import Puesto
from .serializers import PuestoSerializer


    
class PuestosView(APIView):
    serializer_class = PuestoSerializer

    def get_one(self, pk):
        try:
            item = Puesto.objects.get(pk=pk, activo=True)
            return item
        except(Puesto.DoesNotExist):
            return None

    @swagger_auto_schema(responses={200: PuestoSerializer(many=True)})
    def get(self, request, pk=None):
        if  pk:
            item = self.get_one(pk)
            if item == None: 
                return Response({"message":"resource not found"}, status=404)
            serializer = PuestoSerializer(item)
            return Response(serializer.data)

        items = Puesto.objects.filter(activo=True) 
        serializer = PuestoSerializer(items, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PuestoSerializer, responses={201: PuestoSerializer})
    def post(self, request):
        
        serializer = PuestoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=PuestoSerializer, responses={200: PuestoSerializer})
    def put(self, request, pk):
        item = self.get_one(pk)
        if item == None: 
            return Response({"message":"resource not found"}, status=404)
        
        serializer = PuestoSerializer(item, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
 
        return Response(serializer.errors, status=404)
    
    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        item = self.get_one(pk)
        if item == None:
            return Response({"message":"resource not found"}, status=404)
        item.activo = False
        item.eliminado_en = timezone.now()
        item.save()
        return Response(status=204)
