'''
Created on 10 nov 2024

@author: Usuario
'''
from entrega2.tipos.Lista_ordenada import ListaOrdenada

def test_lista_ordenada():
    print("TEST DE LISTA ORDENADA:")
    print("################################################")

    lista = ListaOrdenada.of(lambda x: x)
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Resultado de la lista: {lista}") 

    removed = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed}")  
    removed_all = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_all}")  

    
    lista.add_all([1, 2, 3])
    lista.add(5)
    print(f"Lista después de añadirle el 0: {lista}") 
    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")  
    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")  

if __name__ == '__main__':
    test_lista_ordenada()

