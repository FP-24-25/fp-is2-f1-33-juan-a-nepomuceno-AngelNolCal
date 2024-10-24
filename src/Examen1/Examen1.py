'''
Created on 24 oct 2024

@author: Usuario
'''
from _ast import Try

print(' ')
print('#######################################################')
print('Ejercicio 1')
def calcular_producto(n, k):
    try:
        if not isinstance(n, int) or not isinstance(k, int):
            raise ValueError("Ambos valores deben ser enteros.")
        
        if n <= k :
            raise ValueError("El valor de n debe ser mayor o igual que el valor de k.")
        if k < 0 or n < 0:
            raise ValueError("n y k deben ser positivos")

        
        producto = 1
        
        for i in range(1, k-1):
            producto *= (n - i + 1)
        
        return producto
    
    except ValueError as e:
        return f"Error: {e}"
    
    except Exception as e:
        return f"Se ha producido un error inesperado: {e}"


n = 4
k = 2
resultado = calcular_producto(n, k)
print('el resultado es:')
print(resultado)  

print(' ')
print('#######################################################')
print('Ejercicio 2')


def factorial(num):
    try:
        if num == 0 or num == 1:    
            return 1
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado
    except ValueError as e:
        return f"Error: {e}"

def binomial(n, k):
    try:
        if n < k :
            raise ValueError("El valor de n debe ser mayor o igual que el valor de k.")
        if k < 0 or n < 0:
            raise ValueError("n y k deben ser positivos")
            
        return factorial(n) // (factorial(k + 1) * factorial(n - k))
    except ValueError as e:
        return f"Error: {e}"
n = 5
k = 3
resultado = binomial(n, k)
print('el resultado es:')
print(resultado)

print(' ')
print('#######################################################')
print('Ejercicio 3')

import math

def calcular_S(n, k):
    try:
        if not isinstance(n, int) or not isinstance(k, int):
            raise ValueError("Ambos valores deben ser enteros.")
        if n < k :
            raise ValueError("El valor de n debe ser mayor o igual que el valor de k.")
        if k < 0 or n < 0:
            raise ValueError("n y k deben ser positivos")

        k_factorial = math.factorial(k)
        

        sumatoria = 0
        
        for i in range(k):
            signo = (-1) ** i 
            binomio = math.comb(k, i)
            potencia = (k - i) ** (n + 1)

            sumatoria += signo * binomio * potencia
        
        resultado = (k_factorial / (n * (k + 2))) * sumatoria
        
        return resultado
    
    except ValueError as e:
        return f"Error: {e}"
    
    except Exception as e:
        return f"Se ha producido un error inesperado: {e}"


n = 3
k = -1
resultado = calcular_S(n, k)
print('el resultado es:')
print(resultado)  

print(' ')
print('#######################################################')
print('Ejercicio 4')

import string
from collections import Counter
from typing import List, Tuple

def palabras_mas_comunes(fichero: str, n: int = 5) -> List[Tuple[str, int]]:
    try:

        if n <= 1:
            raise ValueError("El valor de n debe ser mayor que 1.")
        

        with open(fichero, 'r', encoding='utf-8') as file:

            texto = file.read()
        

        texto = texto.lower()
        

        texto = texto.translate(str.maketrans('', '', string.punctuation))
        

        palabras = texto.split()
        

        contador_palabras = Counter(palabras)

        palabras_comunes = contador_palabras.most_common(n)
        
        return palabras_comunes
    
    except FileNotFoundError:
        return [("Error", "No se encontró el archivo.")]
    
    except ValueError as e:
        return [("Error", str(e))]
    
    except Exception as e:
        return [("Error", f"Se ha producido un error inesperado: {e}")]


fichero = 'archivo_palabras.txt'
n = 5
resultado = palabras_mas_comunes(fichero, n)

print(resultado)  






