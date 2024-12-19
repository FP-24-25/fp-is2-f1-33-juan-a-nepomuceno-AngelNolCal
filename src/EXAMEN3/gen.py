'''
Created on 19 dic 2024

@author: Usuario
'''

# gen.py
class Gen:
    def __init__(self, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a cero.")
        self.__nombre = nombre
        self.__tipo = tipo
        self.__num_mutaciones = num_mutaciones
        self.__loc_cromosoma = loc_cromosoma

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def num_mutaciones(self) -> int:
        return self.__num_mutaciones

    @property
    def loc_cromosoma(self) -> str:
        return self.__loc_cromosoma

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> 'Gen':
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(linea: str) -> 'Gen':
        partes = linea.strip().split(",")
        if len(partes) != 4:
            raise ValueError("La línea no tiene el formato esperado.")
        nombre, tipo, num_mutaciones, loc_cromosoma = partes
        return Gen.of(nombre, tipo, int(num_mutaciones), loc_cromosoma)

    def __str__(self) -> str:
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosoma})"
