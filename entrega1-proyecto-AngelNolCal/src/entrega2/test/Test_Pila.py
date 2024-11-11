'''
Created on 11 nov 2024

@author: Usuario
'''

from entrega2.tipos.Pila import Pila

def test_pila():
    print("TEST DE PILA:")

    
    pila = Pila.of()


    assert pila.size() == 0, "La pila debería estar vacía inicialmente."


    pila.add(10)
    pila.add(20)
    pila.add(30)


    assert str(pila) == "Pila([30, 20, 10])", "La representación de la pila es incorrecta."


    elemento = pila.remove()
    assert elemento == 30, "El último elemento agregado debería ser el primero en eliminarse."
    elemento = pila.remove()
    assert elemento == 20, "El segundo elemento agregado debería ser el segundo en eliminarse."


    pila.remove()
    assert pila.is_empty(), "La pila debería estar vacía después de eliminar todos los elementos."


    try:
        pila.remove()
        assert False, "Debería lanzarse una excepción al intentar eliminar de una pila vacía."
    except AssertionError as e:
        assert str(e) == "El agregado está vacío", "El mensaje de excepción es incorrecto."

    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_pila()

