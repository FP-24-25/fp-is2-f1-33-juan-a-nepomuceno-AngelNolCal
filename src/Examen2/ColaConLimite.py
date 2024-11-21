'''
Created on 21 nov 2024

@author: Usuario
'''

from __future__ import annotations
from typing import TypeVar, Generic
from entrega2.tipos.Agregado_lineal import AgregadoLineal

E = TypeVar('E')

class ColaConLimite(AgregadoLineal[E]):
    def __init__(self, capacidad: int):

        #Constructor para inicializar una cola con límite.

        super().__init__()
        self._capacidad = capacidad


    def of(capacidad: int) -> ColaConLimite[E]:

        #Método de factoría para crear una instancia de ColaConLimite con capacidad especificada.

        return ColaConLimite(capacidad)

    def add(self, e: E) -> None:
      
        #Añade un elemento a la cola si no está llena.

        if self.is_full():
            raise OverflowError("La cola está llena, no se pueden añadir más elementos.")
        self._elements.append(e)

    def is_full(self) -> bool:
        
        #Verifica si la cola está llena.

        return self.size() >= self._capacidad

    def __str__(self) -> str:
        
        #Representación en forma de cadena de la cola.
        
        return f"ColaConLimite({self._elements})"


