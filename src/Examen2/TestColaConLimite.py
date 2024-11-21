'''
Created on 21 nov 2024

@author: Usuario
'''
from Examen2.ColaConLimite import ColaConLimite

# Test para la clase ColaConLimite
def test_cola_con_limite():
    print("TEST DE COLA CON LÍMITE:")
    print("################################################")

    # Crear una cola con capacidad máxima de 3 elementos
    cola = ColaConLimite.of(6)
    cola.add(1)
    cola.add(2)
    cola.add("a")
    cola.add(5)


    print(f"Resultado de la cola tras añadir tres elementos: {cola}")

    try:
        cola.add(4)  # Intentar exceder la capacidad
    except OverflowError as e:
        print(f"{e}")

    print(f"La cola está llena: {cola.is_full()}")


if __name__ == '__main__':
    test_cola_con_limite()