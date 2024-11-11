'''
Created on 10 nov 2024

@author: Usuario
'''
from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

def test_lista_ordenada_sin_repeticion():
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")
    
  
    lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)

    
    lista.add(23)
    lista.add(47)
    lista.add(47)      
    lista.add(1)
    lista.add(2)
    lista.add(-3)
    lista.add(4)
    lista.add(5)
    lista.add(-2)


    print(f"Resultado de la lista ordenada sin repetición: {lista}")


    '''print('################################################')
    # Eliminar el primer elemento
    eliminado = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {eliminado}")
    # Salida esperada: 47'''

    print('################################################')

    eliminados = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {eliminados}")
 

    print('################################################')

    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")

    lista.add(0) 
    print(f"Lista después de añadirle el 0: {lista}")


    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")


if __name__ == '__main__':
    test_lista_ordenada_sin_repeticion()