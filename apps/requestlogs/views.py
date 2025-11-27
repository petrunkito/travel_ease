from rest_framework.views import APIView
from rest_framework.response import Response
from .procesar_solicitudes_stack import PilaSolicitudesLogs

from rest_framework.views import APIView
from rest_framework.response import Response

class LogsView(APIView):

    def get(self, request):
        # Obtener el último log (LIFO)
        ultimo_log = PilaSolicitudesLogs().obtener_ultimo()

        if ultimo_log is None:
            return Response({
                "mensaje": "No hay más solicitudes en la pila."
            }, status=404)

        return Response({
            "mensaje": "Log procesado correctamente",
            "detalle": ultimo_log
        }, status=200)
