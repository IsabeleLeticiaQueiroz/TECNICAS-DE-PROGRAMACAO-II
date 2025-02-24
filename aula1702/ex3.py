a1 = float(input("Informe a primeira altura: "))
a2 = float(input("Informe a segunda altura: "))
a3 = float(input("Informe a terceira altura: "))

if a1 > a2 and a1 > a3:
    print(f"Primeiro mais alto: {a1}")
    if a2 > a3:
        print(f"Segundo mais alto: {a2}")
        print(f"Terceiro mais alto: {a3}")
    elif a3 > a2:
        print(f"Segundo mais alto: {a3}")
        print(f"Terceiro mais alto: {a2}")
    else:
        print(f"Segundos mais altos: {a3} e {a2}")
elif a2 > a1 and a2 > a3:
    print(f"Primeiro mais alto: {a2}")
    if a1 > a3:
        print(f"Segundo mais alto: {a1}")
        print(f"Terceiro mais alto: {a3}")
    elif a3 > a1:
        print(f"Segundo mais alto: {a3}")
        print(f"Terceiro mais alto: {a1}")
    else:
        print(f"Segundos mais altos: {a1} e {a3}")
elif a3 > a1 and a3 > a2:
    print(f"Primeiro mais alto: {a3}")
    if a1 > a2:
        print(f"Segundo mais alto: {a1}")
        print(f"Terceiro mais alto: {a2}")
    elif a2 > a1:
        print(f"Segundo mais alto: {a2}")
        print(f"Terceiro mais alto: {a1}")
    else:
        print(f"Segundos mais altos: {a1} e {a2}")
else:
    print("As alturas são iguais")