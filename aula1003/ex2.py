import numpy as np
matriz = []
for i in range(4):
    for j in range(4):
        valor = int(input(f"Digite um valor para a posição ({i+1},{j+1}): "))
        matriz.append(valor)

matriz = np.array(matriz).reshape(4,4)
# imprimir os valores maiores que 10 
if matriz[matriz > 10].size > 0:
    print(f"Os valores maiores que 10 são: {matriz[matriz > 10]}")
# imprmir quantos numeros sao
print(f"Quantidade de numeros maiores que 10: {matriz[matriz > 10].size}")