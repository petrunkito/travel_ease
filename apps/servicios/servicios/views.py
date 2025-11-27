from rest_framework.views import APIView
from rest_framework.response import Response

from apps.servicios.servicios.procesar_solicitudes_queue import ProcesarSolicitudesQueue
from apps.servicios.servicios.procesar_solicitudes_arbol_general import ProcesarSolicitudesArbol


class ProcesarServicioView(APIView):

    def get(self, request):
        # Obtener el siguiente elemento de la cola
        detalle = ProcesarSolicitudesQueue().procesar_siguiente()

        if detalle is None:
            return Response({
                "mensaje": "No hay más servicios en la cola."
            }, status=404)

        # Construimos la respuesta JSON
        data = {
            "tipo_servicio": detalle.tipo_servicio,
            "id_servicio": detalle.id_servicio
        }

        return Response({
            "mensaje": "Servicio procesado correctamente",
            "detalle": data
        }, status=200)


class ProcesarServicioArbolView(APIView):

    def get(self, request):
        # Obtener el siguiente elemento de la cola
        
        detalle2 = ProcesarSolicitudesArbol()

        data = {
            "preorden": detalle2.preorden(), 
            "postorden": detalle2.postorden(),
            "nivel": detalle2.niveles()
        }

        return Response({
            "mensaje": "Servicio procesado correctamente",
            "detalle": data
        }, status=200)
