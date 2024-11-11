'''
Created on 10 nov 2024

@author: Usuario
'''
from __future__ import annotations
from entrega2.tipos.Cola import Cola
from typing import Callable, TypeVar, Generic
from entrega2.tipos.Agregado_lineal import AgregadoLineal

E = TypeVar('E')
R = TypeVar('R')



class ColaPrioridad(Generic[E, R], AgregadoLineal[E]):
    def __init__(self):
        super().__init__()
        self._priorities = []

    def add(self, e: E, priority: R) -> None:
        index = self.__index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def __index_order(self, priority: R) -> int:
        for i, p in enumerate(self._priorities):
            if priority < p:
                return i
        return len(self._priorities)

    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        self._priorities.pop(0)
        return self._elements.pop(0)

    def __str__(self) -> str:
        return f"ColaPrioridad({list(zip(self._elements, self._priorities))})"


