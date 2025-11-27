# services/colas.py
from collections import deque

class ProcesarSolicitudesQueue:
    _instance = None  # atributo estático para guardar la única instancia

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProcesarSolicitudesQueue, cls).__new__(cls)
            cls._instance.cola = deque()  # inicialización de la cola en la instancia única
        return cls._instance

    def agregar_solicitud(self, detalle_servicio):
        self.cola.append(detalle_servicio)

    def procesar_siguiente(self):
        
        if self.cola:
            return self.cola.popleft()
        return None

class TipoServicios:
    Hoteles = 'hoteles'
    Transportes = 'transportes'
    Vuelos = 'vuelos'

class DetalleServicio:
    def __init__(self, tipo_servicio, id_servicio):
        self.tipo_servicio = tipo_servicio
        self.id_servicio = id_servicio

