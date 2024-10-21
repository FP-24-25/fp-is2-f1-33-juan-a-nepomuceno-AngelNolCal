

print('#######################################################')
print('TEST Lecturas 1')
from lecturas.lecturas import aparicionPalabra
cad = 'salud'

resultado = aparicionPalabra('archivo_palabras.txt')
print(f"La palabra {cad} aparece {resultado} veces.")
print(' ')


print('#######################################################')
print('TEST Lecturas 2')
from lecturas.lecturas import lineas_con_palabra
cad= 'proyecto'
resultado, lineas = lineas_con_palabra('archivo_palabras.txt')
print('Las líneas en las que aparece', cad ,' son:')
for linea in lineas:
    print(linea)

print(' ')

print('#######################################################')
print('TEST Lecturas 3')
from lecturas.lecturas import encontrar_palabras_unicas
resultado = encontrar_palabras_unicas('archivo_palabras.txt')
print("Las palabras unicas encontradas son:")
print(resultado)
print(' ')

print('#######################################################')
print('TEST Lecturas 4')
from lecturas.lecturas import longitud_promedio_lineas
resultado = longitud_promedio_lineas('palabras_random.csv')
if resultado is not None:
    print(f"La longitud media de las líneas es: {resultado:.2f} palabras.")