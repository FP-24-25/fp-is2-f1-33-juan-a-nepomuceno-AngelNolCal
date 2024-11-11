'''
Created on 21 oct 2024

@author: Angel
'''

#Ejercicio 1
def calcularproducto(n, k):
    producto = 1
    for i in range(k + 1):
        producto *= (n - i + 1)
    return producto


#Ejercicio 2
def producto_secuencia_geometrica(a1, r, k):
    producto = 1
    for n in range(1, k + 1):
        an = a1 * (r ^ (n - 1))  
        producto *= an          
    return producto


#Ejercicio 3
def factorial(num):
    if num == 0 or num == 1:
        return 1
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado

def binomial(n, k):

    if k < 0 or k > n:
        print('Error parametros incorrectos')
    return factorial(n) // (factorial(k) * factorial(n - k))


def S(n, k):

    suma = 0
    for i in range(k):
        signo = (-1) ** i
        binom = binomial(k + 1, i + 1)
        termino = binom * (k - i) ** n
        suma += signo * termino
    return suma / factorial(k)



#Ejercicio 5
def metododNewton(f, df, a, epsilon):

    x_n = a
    while True:
        f_xn = f(x_n)  
        if abs(f_xn) <= epsilon:
            return x_n  
        
        df_xn = df(x_n) 
        if df_xn == 0:
            raise ValueError("La derivada es cero. No se puede continuar.")
        
       
        x_n = x_n - f_xn / df_xn


import math

def f(x):
    return x**2 - 2 

def df(x):
    return 2 * x 
















