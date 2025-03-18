
num = int(input("Informe um numero pra calculo da tabuada: "))
i = int(input("Informe o começo: "))
limite = int(input("Informe ate onde voce quer sua tabuada: "))
while i <= limite:
 mult = num * i
 print(f"{num} x {i} = {mult}")
 i +=1