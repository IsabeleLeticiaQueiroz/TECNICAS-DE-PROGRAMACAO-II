import numpy as np
linhas = 2
colunas = 3
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = (input(f"Digite um nome de cidade para a posição ({i+1},{j+1}): "))
        linha.append(valor)
    matriz.append(linha)
print(matriz)