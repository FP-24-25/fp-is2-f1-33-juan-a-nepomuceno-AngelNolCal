'''
Created on 19 dic 2024

@author: Usuario
'''
# src/relacion_gen_a_gen.py

# relacion_gen_a_gen.py
class RelacionGenAGen:
    def __init__(self, nombre_gen1: str, nombre_gen2: str, conexion: float):
        if not (-1 <= conexion <= 1):
            raise ValueError("La conexión debe ser un número entre -1 y 1.")
        self.__nombre_gen1 = nombre_gen1
        self.__nombre_gen2 = nombre_gen2
        self.__conexion = conexion

    @property
    def nombre_gen1(self) -> str:
        return self.__nombre_gen1

    @property
    def nombre_gen2(self) -> str:
        return self.__nombre_gen2

    @property
    def conexion(self) -> float:
        return self.__conexion

    @property
    def coexpresados(self) -> bool:
        return self.__conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.__conexion < 0.75

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(linea: str) -> 'RelacionGenAGen':
        partes = linea.strip().split(",")
        if len(partes) != 3:
            raise ValueError("La línea no tiene el formato esperado.")
        nombre_gen1, nombre_gen2, conexion = partes
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, float(conexion))

    def __str__(self) -> str:
        return f"{self.nombre_gen1} - {self.nombre_gen2}: {self.conexion}"

