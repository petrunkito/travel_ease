from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from apps.servicios.servicios.procesar_solicitudes_queue import ProcesarSolicitudesQueue, TipoServicios, DetalleServicio 
from apps.servicios.servicios.procesar_solicitudes_arbol_general import ProcesarSolicitudesArbol

from .models import Hotel
from .serializers import HotelSerializer

class HotelesView(APIView):

    def get_one(self, pk):
        try:
            item = Hotel.objects.get(pk=pk, activo=True)
            return item
        except(Hotel.DoesNotExist):
            return None

    @swagger_auto_schema(responses={200: HotelSerializer(many=True)})
    def get(self, request, pk=None):
        if  pk:
            item = self.get_one(pk)
            if item == None: 
                return Response({"message":"resource not found"}, status=404)
            serializer = HotelSerializer(item)
            return Response(serializer.data)

        items = Hotel.objects.filter(activo=True) 
        serializer = HotelSerializer(items, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=HotelSerializer, responses={201: HotelSerializer})
    def post(self, request):
        
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            hotel = serializer.save()
            detalle_servicio = DetalleServicio(TipoServicios.Hoteles,hotel.id)
            ProcesarSolicitudesQueue().agregar_solicitud(detalle_servicio)
            ProcesarSolicitudesArbol().agregar(TipoServicios.Hoteles, hotel.nombre)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
    @swagger_auto_schema(request_body=HotelSerializer, responses={200: HotelSerializer})
    def put(self, request, pk):
        item = self.get_one(pk)
        if item == None: 
            return Response({"message":"resource not found"}, status=404)
        
        serializer = HotelSerializer(item, data = request.data, partial=True)
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

