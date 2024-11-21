'''
Created on 10 nov 2024

@author: Usuario
'''
from typing import Generic, TypeVar, List, Callable, Optional


E = TypeVar('E')

class AgregadoLineal(Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    def size(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def elements(self) -> List[E]:
        return list(self._elements)

    def add(self, e: E) -> None:
        raise NotImplementedError("Método abstracto. Debe ser implementado por una subclase.")

    def add_all(self, ls: List[E]) -> None:
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        assert not self.is_empty(), "El agregado está vacío"
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed = []
        while not self.is_empty():
            removed.append(self.remove())
        return removed

    def contains(self, e: E) -> bool:
        """Verifica si el elemento dado está en el agregado."""
        return e in self._elements

    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        """Devuelve el primer elemento que cumple la condición dada por la función func."""
        for e in self._elements:
            if func(e):
                return e
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        """Filtra los elementos del agregado según la condición dada por func."""
        return [e for e in self._elements if func(e)]
