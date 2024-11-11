'''
Created on 10 nov 2024

@author: Usuario
'''
from __future__ import annotations
from typing import Callable, TypeVar, Generic
from entrega2.tipos.Agregado_lineal import AgregadoLineal

E = TypeVar('E')

class Cola(AgregadoLineal[E]):
    
    def of() -> Cola[E]:
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self) -> str:
        return f"Cola({self._elements})"

