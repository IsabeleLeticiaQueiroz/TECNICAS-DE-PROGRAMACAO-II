import numpy as np
# instalando a biblioteca numpy

tam = 10
vetor = []
for i in range(tam):
    valor = int(input(f"Digite um valor do {i+1}° numero : "))
    vetor.append(valor)

print(vetor)