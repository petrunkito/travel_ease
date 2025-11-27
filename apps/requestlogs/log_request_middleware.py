from datetime import datetime
from .procesar_solicitudes_stack import PilaSolicitudesLogs

class LogRequestMiddleware:
    RUTAS_EXCLUIDAS = [
        "/api/historial/",       # evitar registrar el endpoint de logs
        "/api/historial",        # por si lo llamás sin slash final
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path not in self.RUTAS_EXCLUIDAS:
            log = {
                "metodo": request.method,
                "ruta": request.path,
                "fecha": datetime.now().isoformat(),
                # "usuario": request.user.username if request.user.is_authenticated else "anónimo",
                "ip": request.META.get("REMOTE_ADDR"),
            }
            PilaSolicitudesLogs().agregar(log)

        response = self.get_response(request)
        return response
