'''
Created on 11 nov 2024

@author: Usuario
'''
from entrega2.tipos.Cola import Cola

def test_cola():
    print("TEST DE COLA:")
    print("################################################")

    cola = Cola.of()
    cola.add_all([23, 47, 1, 2, -3, 4, 5])
    print(f"Resultado de la cola: {cola}")  

    removed_all = cola.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_all}")  

if __name__ == '__main__':
    test_cola()