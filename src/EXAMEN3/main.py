'''
Created on 19 dic 2024

@author: Usuario
'''

# main.py
from archivos import crear_archivos_temporales, leer_genes_archivo, leer_red_genes_archivo
from red_genica import RedGenica

# Crear archivos temporales si no existen
crear_archivos_temporales()


print("Genes")
# Leer genes desde el archivo genes.txt
genes = leer_genes_archivo()
for gen in genes:
    print(gen)

print("")
print(" ")
print("Relaciones entre genes")

# Leer relaciones entre genes desde el archivo red_genes.txt
relaciones = leer_red_genes_archivo()
for relacion in relaciones:
    print(relacion)
    # Imprimir si la relación es coexpresada o antiexpresada
    if relacion.coexpresados:
        print(f"{relacion.nombre_gen1} y {relacion.nombre_gen2} son coexpresados.")
    elif relacion.antiexpresados:
        print(f"{relacion.nombre_gen1} y {relacion.nombre_gen2} son antiexpresados.")
    else:
        print(f"{relacion.nombre_gen1} y {relacion.nombre_gen2} no son coexpresados ni antiexpresados.")

print(" ")
print(" ")
print("Red Genica")

# Comprobación: Construir el objeto RedGenica usando el método parse
red_genica = RedGenica.parse()

# Imprimir el resultado
print(red_genica)
