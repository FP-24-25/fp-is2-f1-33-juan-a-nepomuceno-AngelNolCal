'''
Created on 10 nov 2024

@author: Usuario
'''

from __future__ import annotations
from entrega2.tipos.Lista_ordenada import ListaOrdenada
from typing import Callable, TypeVar, Generic

E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticion(ListaOrdenada[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__(order)
        self._removed_elements = []

    def of(order: Callable[[E], R]) -> Lista_ordenada_sin_repeticion:
        return Lista_ordenada_sin_repeticion(order)

    def add(self, e: E) -> None:
        # Restaurar los elementos eliminados si hay elementos en _removed_elements
        if self._removed_elements:
            self._elements.extend(self._removed_elements)
            self._removed_elements.clear()
            # Ordenar y eliminar duplicados
            self._elements = sorted(set(self._elements), key=self._order)
        

        if e not in self._elements:
            index = self._ListaOrdenada__index_order(e)
            self._elements.insert(index, e)

    def remove_all(self) -> list[E]:
        self._removed_elements = self._elements.copy()
        self._elements.clear()  
        return self._removed_elements

    def __str__(self):
        return f"ListaOrdenadaSinRepeticion({self._elements})"
