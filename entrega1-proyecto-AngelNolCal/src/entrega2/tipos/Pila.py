'''
Created on 10 nov 2024

@author: Usuario
'''
from __future__ import annotations
from typing import Callable, TypeVar, Generic
from entrega2.tipos.Agregado_lineal import AgregadoLineal
E = TypeVar('E')
R = TypeVar('R')


class Pila(AgregadoLineal[E]):

    def of() -> 'Pila[E]':
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __str__(self) -> str:
        return f"Pila({self._elements})"



