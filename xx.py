
#Clase nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []  # lista de hijos

#Clase Arbol
class Arbol:

    def __init__(self, datoRaiz):
        self.raiz = Nodo(datoRaiz)

#Metodo buscar
    def buscar(self, nodo, dato):
        #caso base
        if nodo.dato == dato:
            return nodo

        #Buscar recursivamente en los hijos
        for hijo in nodo.hijos:
            encontrado= self.buscar(hijo, dato)
            if encontrado:
                return encontrado
        return None

#Metodo agregar
    def agregar(self, padre, hijo):
        nodoPadre=self.buscar(self.raiz, padre)
        if nodoPadre:
            nodoPadre.hijos.append(Nodo(hijo))
            print(f"hijo '{hijo}' agregado a '{padre}'.")
        else:
            print ("Padre no encontrado")

    #Recorridos
    #Recorrido en Preorden
    def preorden (self, nodo):
        if nodo is None:
            return

        print (nodo.dato) #Visitar nodo

        for hijo in nodo.hijos: #Recorrer hijos
            self.preorden(hijo)

    #Recorrido en Postorden
    def postorden(self,  nodo):
        if nodo is None:
            return

        for hijo in nodo.hijos: #Recorrer hijos
            self.postorden(hijo)

        print (nodo.dato) #Visitar nodo

    #Recorrido Por niveles, usando una cola
    def niveles(self):
        from collections import deque
        cola= deque([self.raiz]) #Iniciar con la raiz

        while cola:
            nodo= cola.popleft()
            print(nodo.dato)

            for hijo in nodo.hijos:
                cola.append(hijo)

# 1. Crear el Árbol (La Raíz)
# Estructura que vamos a crear:
#        A
#      / | \
#     B  C  D
#    / \ |
#   E   F G

miArbol = Arbol("A")

# 2. Agregar nodos (Construir el árbol)
miArbol.agregar("A", "B") # B es hijo de A
miArbol.agregar("A", "C") # C es hijo de A
miArbol.agregar("A", "D") # D es hijo de A
miArbol.agregar("B", "E") # E es hijo de B
miArbol.agregar("B", "F") # F es hijo de B
miArbol.agregar("C", "G") # G es hijo de C
miArbol.agregar("H", "I") # Padre no encontrado (H no existe)

print("\n--- Resultados de Búsqueda ---")
# 3. Buscar un nodo
nodo_c = miArbol.buscar(miArbol.raiz, "C")
if nodo_c:
    print(f"Buscando 'C': Encontrado. Dato: {nodo_c.dato}, Hijos: {[h.dato for h in nodo_c.hijos]}")
else:
    print("Buscando 'C': No encontrado.")

print("\n--- Recorrido en Preorden (Raíz, Hijos) ---")
miArbol.preorden(miArbol.raiz) # Salida esperada: A B E F C G D

print("\n--- Recorrido en Postorden (Hijos, Raíz) ---")
miArbol.postorden(miArbol.raiz) # Salida esperada: E F B G C D A

print("\n--- Recorrido Por Niveles (BFS) ---")
miArbol.niveles() # Salida esperada: A B C D E F G