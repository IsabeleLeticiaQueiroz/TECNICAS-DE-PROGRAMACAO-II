# aprendendo estrutura if 
p1 = float(input("Informe o peso da primeira pessoa:"))
p2 = float(input("Informe o peso da segunda pessoa:"))

if p1 > p2:
    print(f'A primeira pessoa é mais pesada {p1} kg')
elif p1 == p2: 
    print("As pessoas tem o mesmo peso")
else:
    print(f'A segunda pessoa é mais pesada com {p2} kg')
    