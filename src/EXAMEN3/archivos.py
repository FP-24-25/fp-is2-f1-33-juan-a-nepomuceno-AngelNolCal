# archivos.py
import os

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
MYC,oncogen,134,8q24.21
CCND1,oncogen,95,11q13
ATM,supresor tumoral,121,11q22.3
RB1,supresor tumoral,158,13q14.2
APC,supresor tumoral,119,5q22.2
NF1,supresor tumoral,83,17q11.2
MET,oncogen,78,7q31.2
ALK,oncogen,62,2p25.1
ROS1,oncogen,55,6q22.33
RET,oncogen,49,10q11.21
ERBB2,oncogen,108,17q12
VHL,supresor tumoral,91,3p25.3
MLH1,supresor tumoral,76,3p21.32
MSH2,supresor tumoral,69,2p22
PMS2,supresor tumoral,52,7p22
MLH3,supresor tumoral,47,22q13.31
MSH6,supresor tumoral,39,2p16
EPCAM,supresor tumoral,42,20p13
CTNNB1,oncogen,38,3p21.1""")

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
CCND1,MYC,-0.8
ATM,MYC,0.8
ATM,RB1,-0.9
APC,NF1,0.6
NF1,MET,0.6
MET,ALK,0.6
ROS1,RET,0.9
ERBB2,RET,0.9
ERBB2,VHL,-0.8
VHL,MSH2,0.8
MLH1,MSH2,0.7
MLH1,PMS2,0.7
PMS2,MLH3,0.8
MSH6,MLH3,0.9
MSH6,EPCAM,-0.8
CTNNB1,EPCAM,0.8""")

def leer_genes_archivo():
    """Lee el archivo genes.txt y devuelve una lista de objetos Gen."""
    from gen import Gen
    with open("genes.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    return [Gen.parse(linea) for linea in lineas]

def leer_red_genes_archivo():
    """Lee el archivo red_genes.txt y devuelve una lista de objetos RelacionGenAGen."""
    from relacion_gen_a_gen import RelacionGenAGen
    with open("red_genes.txt", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    return [RelacionGenAGen.parse(linea) for linea in lineas]
