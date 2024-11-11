'''
Created on 21 oct 2024

@author: Angel
'''


def aparicionPalabra(fichero):
    contador = 0
    
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
            
                palabras = linea.strip().split()
               
                contador += palabras.count(cad)
    except FileNotFoundError:
        print(f"El archivo '{fichero}' no fue encontrado.")
    
    return contador



def lineas_con_palabra(fichero):
    contador = 0
    lineas_con_palabra = []
    
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                if cad in linea:
                    contador += 1
                    lineas_con_palabra.append(linea.strip())
    except FileNotFoundError:
        print(f"El archivo '{fichero}' no fue encontrado.")
    
    return contador, lineas_con_palabra
cad = 'salud'
resultado, lineas = lineas_con_palabra('archivo_palabras.txt')


   
    
def encontrar_palabras_unicas(fichero):
    palabras_unicas = set()  
    
    try:
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                palabras = linea.strip().split()
                for palabra in palabras:
                    palabras_unicas.add(palabra)
    except FileNotFoundError:
        print(f"El archivo '{fichero}' no fue encontrado.")
    
    return list(palabras_unicas)



from typing import Optional

def longitud_promedio_lineas(file_path: str) -> Optional[float]:
    total_palabras = 0
    total_lineas = 0
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for linea in f:
 
                palabras = linea.strip().split(',')
                total_palabras += len(palabras)
                total_lineas += 1
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no fue encontrado.")
        return None
    

    if total_lineas > 0:
        return total_palabras / total_lineas
    else:
        return 0.0


