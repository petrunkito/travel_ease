from apps.servicios.servicios.procesar_solicitudes_queue import  TipoServicios 
#Codigo de grafo:

class ProcesarSolicitudesGrafoDirigido:

    _instancia = None  # Atributo estático para guardar la instancia única

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super(ProcesarSolicitudesGrafoDirigido, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        # Evitar re-inicialización cada vez que se llama al constructor
        if not hasattr(self, 'adyacencia'):
            self.adyacencia = {}
            self._crear_nodos_base()


    def _crear_nodos_base(self):
        nodos_base = [
            TipoServicios.Vuelos.lower(),
            TipoServicios.Hoteles.lower(),
            TipoServicios.Transportes.lower()
        ]
        for nodo in nodos_base:
            self.agregar_nodo(nodo)

    # def __init__(self):
    #     self.adyacencia= {} #cada nodo tendra una lista de sus vecinos

#Metodo agregar nodo
    def agregar_nodo(self, nodo):
        if nodo not in self.adyacencia:
            self.adyacencia[nodo]= []

#Metodo aregar arista
    def agregar_arista(self, origen, destino):
    # Asegurarnos de que el nodo origen exista
        if origen not in self.adyacencia:
            self.agregar_nodo(origen)
    
    # Solo agregar destino a la lista de adyacencia, sin crear un nodo nuevo
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
  
    #Obtener adyacencias
    def adyacentes(self, nodo):
        if nodo in self.adyacencia:
            return self.adyacencia[nodo]
        return []

#Metodo buscar, solo se usa en el metodo "agregar_arista_nodo"
    def buscar(self, nodo):
        if nodo in self.adyacencia:
            return self.adyacencia[nodo]
        return None

    #Metodo agregar arista a un nodo existente, por si el usuario se equivoca al ingresar el nodo origen
    def agregar_arista_nodo(self, origen, destino):
        nodo_origen=self.buscar(origen)
        if nodo_origen is not None:
            nodo_origen.append((destino))
            print(f"Destino '{destino}' agregado a origen'{origen}'.")
        else:
            print ("Origen no encontrado")

    #-------------------------------------------------------
    def mostrar(self):
        lista_general = []
        for nodo, vecinos in self.adyacencia.items():
            lista_general.append([nodo, vecinos])

            print(f"{nodo} -> {vecinos}")
        return lista_general
