from datetime import date, datetime
from typing import Dict, List, Optional, Set, Tuple, Union, TypeVar, Generic

# Definición de los tipos genéricos
V = TypeVar('V')  # Representa el tipo de vértice
E = TypeVar('E')  # Representa el tipo de arista

# Clase Grafo
class Grafo(Generic[V, E]):
    def __init__(self, dirigido: bool = False):
        self.dirigido = dirigido
        self.vertices: Set[V] = set()
        self.aristas: Dict[Tuple[V, V], E] = {}

    def add_vertex(self, vertex: V) -> bool:
        if vertex in self.vertices:
            return False
        self.vertices.add(vertex)
        return True

    def add_edge(self, origen: V, destino: V, arista: E) -> bool:
        if origen not in self.vertices or destino not in self.vertices or origen == destino:
            return False

        edge = (origen, destino)
        if edge in self.aristas:
            return False

        self.aristas[edge] = arista
        if not self.dirigido:
            self.aristas[(destino, origen)] = arista

        return True

    def contains_edge(self, origen: V, destino: V) -> bool:
        return (origen, destino) in self.aristas

    def vertex_set(self) -> Set[V]:
        return self.vertices

    def successors(self, vertex: V) -> Set[V]:
        return {dest for (src, dest) in self.aristas if src == vertex}

    def predecessors(self, vertex: V) -> Set[V]:
        if self.dirigido:
            return {src for (src, dest) in self.aristas if dest == vertex}
        return self.successors(vertex)

# Clase Usuario
class Usuario:
    def __init__(self, dni: str, nombre: str, apellidos: str, fecha_nacimiento: date):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento

    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> 'Usuario':
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)

    @staticmethod
    def parse(data: str) -> 'Usuario':
        dni, nombre, apellidos, fecha_nacimiento = data.split(',')
        fecha_nacimiento = datetime.strptime(fecha_nacimiento.strip(), "%Y-%m-%d").date()
        return Usuario(dni.strip(), nombre.strip(), apellidos.strip(), fecha_nacimiento)

    def __repr__(self):
        return f"{self.dni} - {self.nombre}"

# Clase Relación
class Relacion:
    _id_counter = 1

    def __init__(self, interacciones: int, dias_activa: int):
        self.id = Relacion._id_counter
        self.interacciones = interacciones
        self.dias_activa = dias_activa
        Relacion._id_counter += 1

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> 'Relacion':
        return Relacion(interacciones, dias_activa)

    def __repr__(self):
        return f"({self.id} - días activa: {self.dias_activa} - num interacciones {self.interacciones})"

# Clase Red Social
class RedSocial(Grafo[Usuario, Relacion]):
    def __init__(self, dirigido: bool = False):
        super().__init__(dirigido)
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(dirigido: bool = False) -> 'RedSocial':
        return RedSocial(dirigido)

    @staticmethod
    def parse(users_data: List[str], relations_data: List[Tuple[str, str, int, int]]) -> 'RedSocial':
        red = RedSocial()
        for user_data in users_data:
            user = Usuario.parse(user_data)
            red.usuarios_dni[user.dni] = user
            red.add_vertex(user)

        for dni_origen, dni_destino, interacciones, dias_activa in relations_data:
            origen = red.usuarios_dni[dni_origen]
            destino = red.usuarios_dni[dni_destino]
            relacion = Relacion.of(interacciones, dias_activa)
            red.add_edge(origen, destino, relacion)

        return red

    def __repr__(self):
        return "\n".join([f"{str(usuario)}" for usuario in self.vertices])

# Probando las clases básicas con ejemplos iniciales
usuarios_ejemplo = [

    "45718832U,Carlos,Lopez,1984-01-14",
    "18909774Z,Maria,Diaz,1995-01-05",
    "25143909I,Lucia,Lopez,1955-06-07",
    "60412985S,Maria,Lopez,1990-05-21",
    "95157732O,Pedro,Gomez,1982-11-13",
    "58127458W,Maria,Garcia,1989-03-18",
    "56427434U,Elena,Fernandez,1978-08-30",
    "71894470A,Carlos,Sanchez,1980-04-25",
    "82007713N,Carlos,Jimenez,1975-10-10",
    "16274768S,Juan,Martinez,1992-02-05",
    "76929765H,Juan,Perez,1994-07-16",
    "63506915L,Lucia,Martinez,1991-11-07",
    "62258675I,Laura,Lopez,1985-09-30",
    "92322186A,Pedro,Diaz,1980-05-05",
    "85707754E,Jorge,Garcia,1993-06-14",
    "61832964Y,Pedro,Lopez,1987-12-03",
    "10115245D,Ana,Lopez,1996-05-15",
    "87345530M,Ana,Garcia,1998-01-11"
]

relaciones_ejemplo = [
    ("45718832U", "18909774Z", 5, 10),
    ("18909774Z", "25143909I", 3, 15),
    ("45718832U", "25143909I", 2, 20),
    ("60412985S", "95157732O", 7, 8),
    ("58127458W", "56427434U", 3, 14),
    ("71894470A", "25143909I", 4, 5),
    ("82007713N", "25143909I", 1, 10),
    ("16274768S", "76929765H", 6, 12),
    ("76929765H", "60412985S", 8, 7),
    ("63506915L", "62258675I", 2, 4),
    ("92322186A", "85707754E", 5, 10),
    ("85707754E", "10115245D", 3, 9),
    ("61832964Y", "87345530M", 4, 5),
    ("10115245D", "45718832U", 6, 2),
    ("87345530M", "56427434U", 2, 3),
]

red_social = RedSocial.parse(usuarios_ejemplo, relaciones_ejemplo)
red_social


# Funciones de testeo para las clases y su integración

def test_vertices_y_vecinos(red: RedSocial):
    # Verificar número de vecinos para cada vértice
    print("************** Nº Vecinos de cada vértice")
    for usuario in red.vertex_set():
        vecinos = red.successors(usuario)
        print(f"{usuario.dni} - {usuario.nombre} -- {len(vecinos)}")

def test_predecesores(red: RedSocial):
    # Verificar número de predecesores para cada vértice
    print("************** Nº Predecesores de cada vértice")
    for usuario in red.vertex_set():
        predecesores = red.predecessors(usuario)
        print(f"{usuario.dni} - {usuario.nombre} -- {len(predecesores)}")

# Ejecutar los tests básicos
test_vertices_y_vecinos(red_social)
print()  # Espacio entre las pruebas
test_predecesores(red_social)


# Clases base proporcionadas previamente
from collections import deque

# Clase Recorrido base
class Recorrido(Generic[V, E]):
    def __init__(self, grafo: Grafo[V, E]):
        self.grafo = grafo
        self.tree: Dict[V, Tuple[Optional[V], float]] = {}
        self.path: List[V] = []

    def path_to_origin(self, source: V) -> List[V]:
        path = []
        current = source
        while current is not None:
            path.append(current)
            current = self.tree.get(current, (None, ))[0]
        return list(reversed(path))

# Clase para Recorrido en Anchura (BFS)
class RecorridoEnAnchura(Recorrido[V, E]):
    def traverse(self, source: V):
        self.tree = {source: (None, 0)}
        queue = deque([source])

        while queue:
            current = queue.popleft()
            for neighbor in self.grafo.successors(current):
                if neighbor not in self.tree:
                    self.tree[neighbor] = (current, self.tree[current][1] + 1)
                    queue.append(neighbor)

# Clase para Recorrido en Profundidad (DFS)
class RecorridoEnProfundidad(Recorrido[V, E]):
    def traverse(self, source: V):
        self.tree = {source: (None, 0)}
        stack = [source]

        while stack:
            current = stack.pop()
            for neighbor in self.grafo.successors(current):
                if neighbor not in self.tree:
                    self.tree[neighbor] = (current, self.tree[current][1] + 1)
                    stack.append(neighbor)

# Función para testear Recorrido en Anchura
def test_recorrido_en_anchura(red: RedSocial):
    origen = red.usuarios_dni["62258675I"]  # Usuario: Lucia Lopez
    destino = red.usuarios_dni["63506915L"]  # Usuario: Ana Garcia

    bfs = RecorridoEnAnchura(red)
    bfs.traverse(origen)

    if destino in bfs.tree:
        camino = bfs.path_to_origin(destino)
        print(f"El camino más corto desde {origen.dni} hasta {destino.dni} es: {[str(u) for u in camino]}")
        print(f"La distancia mínima es: {bfs.tree[destino][1]} pasos.")
    else:
        print(f"No hay conexión directa entre {origen.dni} y {destino.dni}.")

# Función para testear Recorrido en Profundidad
def test_recorrido_en_profundidad(red: RedSocial):
    origen = red.usuarios_dni["25143909I"]  # Usuario: Lucia Lopez
    destino = red.usuarios_dni["76929765H"]  # Usuario: Juan Perez

    dfs = RecorridoEnProfundidad(red)
    dfs.traverse(origen)

    if destino in dfs.tree:
        camino = dfs.path_to_origin(destino)
        print(f"El camino desde {origen.dni} hasta {destino.dni} en profundidad es: {[str(u) for u in camino]}")
    else:
        print(f"No hay conexión directa entre {origen.dni} y {destino.dni}.")

# Ejecutar los tests
test_recorrido_en_anchura(red_social)
print()
test_recorrido_en_profundidad(red_social)

