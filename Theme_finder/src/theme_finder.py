#!/usr/bin/python3

#importar modulos 




#BLOQUE 2, TRATAMIENTO DE TEXTOS

with open("Ejemplos_paper.txt", 'r') as f:
    texto = f.read()


texto = texto.splitlines()
print(texto)

