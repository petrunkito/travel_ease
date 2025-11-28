from apps.servicios.servicios.procesar_solicitudes_queue import  TipoServicios 
#Codigo de grafo:

#Clase grafo
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

    # def __init__(self):
    #     self.adyacencia= {} #cada nodo tendra una lista de sus vecinos

#Metodo agregar nodo
    def agregar_nodo(self, nodo):
        if nodo not in self.adyacencia:
            self.adyacencia[nodo]= []

#Metodo aregar arista
    def agregar_arista(self, origen, destino):
        #Asegurar que los nodos existan
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)

        #Agregar una arista dirigida: origen -> destino
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

#Ejemplo de uso
grafo = ProcesarSolicitudesGrafoDirigido()

# Agregar nodos base
grafo.agregar_nodo(TipoServicios.Vuelos.lower())
grafo.agregar_nodo(TipoServicios.Transportes.lower())
grafo.agregar_nodo(TipoServicios.Hoteles.lower())


# grafo.agregar_nodo("A")
# grafo.agregar_nodo("B")
# grafo.agregar_nodo("C")

# # Agregar aristas
# grafo.agregar_arista("A", "B")   # A -> B
# grafo.agregar_arista("A", "C")   # A -> C
# grafo.agregar_arista("B", "C")   # B -> C
# grafo.agregar_arista("C", "A")   # C -> A (ciclo)
# grafo.agregar_arista("C", "C")   # C -> A (ciclo)

# print(grafo.mostrar())