i = 0
while i <=4: 
    i+=1
    q = input(f"Resposta da {i}° questao: ")
    pont = 0
    if i == 1 | q == 'A':
        pont +=1
    if i == 2 |q == 'C':
        pont +=1
    if i == 3 | q == "D":
        pont +=1
    i +=1
print(f"Voce fez {pont} pontos")
    