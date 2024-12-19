import os

class Gen:
    def __init__(self, nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a cero.")
        self.__nombre = nombre
        self.__tipo = tipo
        self.__num_mutaciones = num_mutaciones
        self.__loc_cromosoma = loc_cromosoma

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def num_mutaciones(self) -> int:
        return self.__num_mutaciones

    @property
    def loc_cromosoma(self) -> str:
        return self.__loc_cromosoma

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str) -> 'Gen':
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)  # Usar cadena 'Gen'

    @staticmethod
    def parse(linea: str) -> 'Gen':  # También aquí, usar 'Gen' como cadena
        partes = linea.strip().split(",")
        if len(partes) != 4:
            raise ValueError("La línea no tiene el formato esperado.")
        nombre, tipo, num_mutaciones, loc_cromosoma = partes
        return Gen.of(nombre, tipo, int(num_mutaciones), loc_cromosoma)

    def __str__(self) -> str:
        return f"{self.nombre}: ({self.tipo},{self.num_mutaciones},{self.loc_cromosoma})"



def crear_archivos_temporales():
    """Crea los archivos genes.txt y red_genes.txt si no existen."""
    if not os.path.exists("genes.txt"):
        with open("genes.txt", "w", encoding="utf-8") as f:
            f.write("""TP53,supresor tumoral,256,17p13.1
EGFR,oncogen,187,7p12
KRAS,oncogen,92,12p12.1
BRAF,oncogen,75,7q34
PIK3CA,oncogen,112,3q26
CDKN2A,supresor tumoral,145,9p21.3
SMAD4,supresor tumoral,89,18q21.1
PTEN,supresor tumoral,102,10q23.31
BCL2,oncogen,67,18q21.32
MYC,oncogen,134,8q24.21""")

    if not os.path.exists("red_genes.txt"):
        with open("red_genes.txt", "w", encoding="utf-8") as f:
            f.write("""TP53,EGFR,0.5
TP53,KRAS,0.7
BRAF,KRAS,0.8
BRAF,TP53,0.4
PIK3CA,TP53,0.2
CDKN2A,SMAD4,0.3
SMAD4,PTEN,0.8
PIK3CA,SMAD4,0.7
BCL2,MYC,0.9
CCND1,MYC,-0.8""")

# Crear archivos temporales si no existen
crear_archivos_temporales()

# Probar la clase Gen con el método parse
if __name__ == "__main__":
    with open("genes.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    for linea in lineas:
        gen = Gen.parse(linea)
        print(gen)




class RelacionGenAGen:
    def __init__(self, nombre_gen1: str, nombre_gen2: str, conexion: float):
        if not (-1 <= conexion <= 1):
            raise ValueError("La conexión debe estar en el rango [-1, 1].")
        self.__nombre_gen1 = nombre_gen1
        self.__nombre_gen2 = nombre_gen2
        self.__conexion = conexion

    @property
    def nombre_gen1(self) -> str:
        return self.__nombre_gen1

    @property
    def nombre_gen2(self) -> str:
        return self.__nombre_gen2

    @property
    def conexion(self) -> float:
        return self.__conexion

    @property
    def coexpresados(self) -> bool:
        return self.__conexion > 0.75

    @property
    def antiexpresados(self) -> bool:
        return self.__conexion < 0.75

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float) -> 'RelacionGenAGen':
        """Método factoría que crea una nueva instancia de RelacionGenAGen."""
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(linea: str) -> 'RelacionGenAGen':
        """Método para parsear una línea de texto y crear una instancia de RelacionGenAGen."""
        partes = linea.strip().split(",")
        if len(partes) != 3:
            raise ValueError("La línea no tiene el formato esperado.")
        nombre_gen1, nombre_gen2, conexion = partes
        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, float(conexion))

    def __str__(self) -> str:
        return f"({self.nombre_gen1} - {self.nombre_gen2}): {self.conexion}"

# Prueba del método parse
if __name__ == "__main__":
    # Ejemplo de línea para parsear
    linea = "TP53,EGFR,0.8"
    relacion = RelacionGenAGen.parse(linea)
    print(relacion)  # Salida esperada: (TP53 - EGFR): 0.8
    print("Coexpresados:", relacion.coexpresados)  # True
    print("Antiexpresados:", relacion.antiexpresados)  # False
