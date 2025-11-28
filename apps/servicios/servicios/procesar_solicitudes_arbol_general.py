from collections import deque
from apps.servicios.servicios.procesar_solicitudes_queue import TipoServicios

# 1. Clase Nodo (sin cambios, representa un elemento del catálogo)
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []  

# 2. Clase Arbol (Implementada como Singleton)
class ProcesarSolicitudesArbol:
    _instancia = None
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(ProcesarSolicitudesArbol, cls).__new__(cls)
        return cls._instancia

    def __init__(self, datoRaiz="servicios"):
        if not hasattr(self, '_inicializado'):
            self.raiz = Nodo(datoRaiz)
            self._inicializado = True
            self.agregar_hijos_predeterminados()

    def agregar_hijos_predeterminados(self):
        
        self.agregar("servicios", TipoServicios.Vuelos.lower())
        self.agregar("servicios", TipoServicios.Transportes.lower())
        self.agregar("servicios", TipoServicios.Hoteles.lower())


    
    
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
      
        
        nodoPadre = self.buscar(self.raiz, padre)
        if nodoPadre:
            nodoPadre.hijos.append(Nodo(hijo))
            return True
        else:
            return False
        
    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self,  nodo, listado):
        if nodo is None:
            return
        

        for hijo in nodo.hijos: 
            self._postorden(hijo, listado)

        print (nodo.dato) 
        listado.append(nodo.dato) 


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

        cola = deque([self.raiz])
        resultado = []
        while cola:
            nodo = cola.popleft()
            print(f" -> {nodo.dato}")
            resultado.append(nodo.dato)
            for hijo in nodo.hijos:
                cola.append(hijo)
        return resultado

