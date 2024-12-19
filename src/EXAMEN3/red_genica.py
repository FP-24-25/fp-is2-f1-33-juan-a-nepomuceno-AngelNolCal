'''
Created on 19 dic 2024

@author: Usuario
'''
# red_genica.py
from archivos import leer_genes_archivo, leer_red_genes_archivo
from gen import Gen
from relacion_gen_a_gen import RelacionGenAGen

class RedGenica:
    def __init__(self):
        self.genes_por_nombre = {}  # Diccionario para almacenar genes por nombre
        self.aristas = []  # Lista para almacenar las relaciones entre genes

    def add_vertice(self, nombre_gen: str, gen: Gen):
        """Añade un vértice (gen) al grafo."""
        self.genes_por_nombre[nombre_gen] = gen

    def add_arista(self, nombre_gen1: str, nombre_gen2: str, conexion: float):
        """Añade una arista (relación entre dos genes) al grafo."""
        relacion = RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)
        self.aristas.append(relacion)

    @staticmethod
    def of():
        """
        Construye un grafo no dirigido y recorrido hacia adelante.
        Devuelve un objeto de tipo RedGenica.
        """
        red_genica = RedGenica()

        # Leer genes y relaciones
        genes = leer_genes_archivo()  # Función de archivos.py
        relaciones = leer_red_genes_archivo()  # Función de archivos.py

        # Añadir los genes al grafo como vértices
        for gen in genes:
            red_genica.add_vertice(gen.nombre, gen)

        # Añadir las relaciones como aristas
        for relacion in relaciones:
            red_genica.add_arista(relacion.nombre_gen1, relacion.nombre_gen2, relacion.conexion)

        return red_genica

    @staticmethod
    def parse():
        """
        Carga la información de los archivos genes.txt y red_genes.txt
        y construye un objeto de tipo RedGenica.
        """
        red_genica = RedGenica()

        # Leer genes desde el archivo genes.txt
        genes = leer_genes_archivo()
        for gen in genes:
            red_genica.add_vertice(gen.nombre, gen)

        # Leer relaciones desde el archivo red_genes.txt
        relaciones = leer_red_genes_archivo()
        for relacion in relaciones:
            red_genica.add_arista(relacion.nombre_gen1, relacion.nombre_gen2, relacion.conexion)

        return red_genica

    def __str__(self):
        # Imprime los vértices (genes) y las aristas (relaciones)
        vertices_str = "Vertices:\n"
        for gen in self.genes_por_nombre.values():
            vertices_str += str(gen) + "\n"

        aristas_str = "Aristas:\n"
        for arista in self.aristas:
            aristas_str += str(arista) + "\n"

        return vertices_str + aristas_str
