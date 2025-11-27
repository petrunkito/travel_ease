from collections import deque
from apps.servicios.servicios.procesar_solicitudes_queue import ProcesarSolicitudesQueue, TipoServicios, DetalleServicio 

# 1. Clase Nodo (sin cambios, representa un elemento del catálogo)
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []  # Lista de nodos hijos

# 2. Clase Arbol (Implementada como Singleton)
class ProcesarSolicitudesArbol:
    _instancia = None  # Variable de clase para almacenar la única instancia

    # Método __new__ para asegurar el Singleton
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(ProcesarSolicitudesArbol, cls).__new__(cls)
        return cls._instancia

    def __init__(self, datoRaiz="servicios"):
        # Aseguramos que la inicialización solo corra una vez
        if not hasattr(self, '_inicializado'):
            self.raiz = Nodo(datoRaiz)
            self._inicializado = True
            
            # Construcción de la estructura predeterminada (Servicios de Agencia)
            self.agregar_hijos_predeterminados()

    def agregar_hijos_predeterminados(self):
        """Método que agrega los nodos base de la agencia de viajes."""
        
        # Hijos de la raíz "Servicios"
        self.agregar("servicios", TipoServicios.Vuelos.lower())
        self.agregar("servicios", TipoServicios.Transportes.lower())
        self.agregar("servicios", TipoServicios.Hoteles.lower())

        # Estructura de ejemplo para "Vuelos"
        # self.agregar("vuelos", "Nacional")
        # self.agregar("vuelos", "Internacional")
        
        # # Estructura de ejemplo para "Hoteles"
        # self.agregar("Hoteles", "3 estrellas")
        # self.agregar("Hoteles", "5 estrellas")


    # --- Métodos de Árbol (Conservados del código anterior) ---
    
    def buscar(self, nodo, dato):
        """Busca un nodo por su dato usando DFS."""
        if nodo.dato == dato:
            return nodo

        for hijo in nodo.hijos:
            encontrado = self.buscar(hijo, dato)
            if encontrado:
                return encontrado
        return None

    def agregar(self, padre, hijo):
        """Agrega un nuevo nodo hijo a un nodo padre existente."""
        # Se asume que 'padre' es el dato del nodo padre (string)
        # y 'hijo' es el dato del nuevo nodo (string)
        
        nodoPadre = self.buscar(self.raiz, padre)
        if nodoPadre:
            # Creamos un nuevo Nodo para el hijo
            nodoPadre.hijos.append(Nodo(hijo))
            # print(f"Hijo '{hijo}' agregado a '{padre}'.")
            return True
        else:
            # print (f"Padre '{padre}' no encontrado. No se pudo agregar '{hijo}'.")
            return False
        
    #Recorrido en Postorden
    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self,  nodo, listado):
        if nodo is None:
            return
        

        for hijo in nodo.hijos: #Recorrer hijos
            self._postorden(hijo, listado)

        print (nodo.dato) #Visitar nodo
        listado.append(nodo.dato) #


    def preorden (self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    
    def _preorden (self, nodo, listado):
        """Recorrido en Preorden (Raíz, Hijos)."""
        if nodo is None:
            return

        print (nodo.dato)
        listado.append(nodo.dato)
        for hijo in nodo.hijos:
            self._preorden(hijo, listado)

    
    def niveles(self):

        """Recorrido Por Niveles (BFS)."""
        cola = deque([self.raiz])
        print("Recorrido por Niveles (BFS):")
        resultado = []
        while cola:
            nodo = cola.popleft()
            print(f" -> {nodo.dato}")
            resultado.append(nodo.dato)
            for hijo in nodo.hijos:
                cola.append(hijo)
        return resultado

