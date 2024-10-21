'''
Created on 21 oct 2024

@author: Usuario
'''
from funciones.funciones import calcularproducto
n = 3
k = 2
resultado = calcularproducto(n, k)

print('#######################################################')
print('TEST 1')
print(f"El producto es: {resultado}")

from funciones.funciones import producto_secuencia_geometrica
print(' ')
print('#######################################################')
print('TEST 2')
a1 = 5
r = 2 
k = 2
resultado = producto_secuencia_geometrica(a1, r, k)
print(f"El producto de los primeros {k} términos es: {resultado}")

print(' ')
print('#######################################################')
print('TEST 3')
from funciones.funciones import binomial

n = 6
k = 2
resultado = binomial(n, k)
print(f"El número combinatorio C({n}, {k}) es: {resultado}")


print(' ')
print('#######################################################')
print('TEST 4')
from funciones.funciones import S
n = 5
k = 3
resultado = S(n, k)
print(f"S({n}, {k}) = {resultado}")

print(' ')
print('#######################################################')
print('TEST 5')
from funciones.funciones import metododNewton
from funciones.funciones import f
from funciones.funciones import df
a = 1.0 
epsilon = 1e-6  

raiz = metododNewton(f, df, a, epsilon)
print(f"La raíz encontrada es: {raiz}")