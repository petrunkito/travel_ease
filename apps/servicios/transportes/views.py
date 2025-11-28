from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone
from apps.servicios.servicios.procesar_solicitudes_queue import ProcesarSolicitudesQueue, TipoServicios, DetalleServicio
from apps.servicios.servicios.procesar_solicitudes_arbol_general import ProcesarSolicitudesArbol
from apps.servicios.servicios.procesar_solicitudes_grafo_dirigido import ProcesarSolicitudesGrafoDirigido


from .models import Transporte
from .serializers import TransporteSerializer
#quede en probar la api de transporte



class TransportesView(APIView):

    def get_one(self, pk):
        try:
            item = Transporte.objects.get(pk=pk, activo=True)
            return item
        except(Transporte.DoesNotExist):
            return None

    @swagger_auto_schema(responses={200: TransporteSerializer(many=True)})
    def get(self, request, pk=None):
        if  pk:
            item = self.get_one(pk)
            if item == None: 
                return Response({"message":"resource not found"}, status=404)
            serializer = TransporteSerializer(item)
            return Response(serializer.data)

        items = Transporte.objects.filter(activo=True) 
        serializer = TransporteSerializer(items, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TransporteSerializer, responses={201: TransporteSerializer})
    def post(self, request):
        
        serializer = TransporteSerializer(data=request.data)
        if serializer.is_valid():
            transporte = serializer.save()
            detalle_servicio = DetalleServicio(TipoServicios.Transportes,transporte.id)
            ProcesarSolicitudesQueue().agregar_solicitud(detalle_servicio)
            ProcesarSolicitudesArbol().agregar(TipoServicios.Transportes, transporte.tipo_transporte.nombre)
            ProcesarSolicitudesGrafoDirigido().agregar_arista(TipoServicios.Transportes, transporte.tipo_transporte.nombre)
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
    @swagger_auto_schema(request_body=TransporteSerializer, responses={200: TransporteSerializer})
    def put(self, request, pk):
        item = self.get_one(pk)
        if item == None: 
            return Response({"message":"resource not found"}, status=404)
        
        serializer = TransporteSerializer(item, data = request.data, partial=True)
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

