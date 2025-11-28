from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from apps.servicios.servicios.procesar_solicitudes_queue import ProcesarSolicitudesQueue, TipoServicios, DetalleServicio 
from .models import Vuelo
from apps.servicios.servicios.procesar_solicitudes_arbol_general import ProcesarSolicitudesArbol
from apps.servicios.servicios.procesar_solicitudes_grafo_dirigido import ProcesarSolicitudesGrafoDirigido
from .serializers import VueloSerializer

class VuelosView(APIView):

    def get_one(self, pk):
        try:
            item = Vuelo.objects.get(pk=pk, activo=True)
            return item
        except(Vuelo.DoesNotExist):
            return None

    @swagger_auto_schema(responses={200: VueloSerializer(many=True)})
    def get(self, request, pk=None):
        if  pk:
            item = self.get_one(pk)
            if item == None: 
                return Response({"message":"resource not found"}, status=404)
            serializer = VueloSerializer(item)
            return Response(serializer.data)

        items = Vuelo.objects.filter(activo=True) 
        serializer = VueloSerializer(items, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=VueloSerializer, responses={201: VueloSerializer})
    def post(self, request):
        
        serializer = VueloSerializer(data=request.data)
        if serializer.is_valid():
            vuelo = serializer.save()
            detalle_servicio = DetalleServicio(TipoServicios.Vuelos,vuelo.id)
            ProcesarSolicitudesQueue().agregar_solicitud(detalle_servicio)
            ProcesarSolicitudesArbol().agregar(TipoServicios.Vuelos, vuelo.destino)
            ProcesarSolicitudesGrafoDirigido().agregar_arista(TipoServicios.Vuelos.lower(), vuelo.destino)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
    @swagger_auto_schema(request_body=VueloSerializer, responses={200: VueloSerializer})
    def put(self, request, pk):
        item = self.get_one(pk)
        if item == None: 
            return Response({"message":"resource not found"}, status=404)
        
        serializer = VueloSerializer(item, data = request.data, partial=True)
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

