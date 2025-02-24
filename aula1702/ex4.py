n1 = float(input("Informe o primeiro número positivo: "))
n2 = float(input("Informe o segundo número positivo: "))

print("Escolha uma das opções abaixo:")
print("1- Media ponderada com peso 2 e 3")
print("2- quadrado da soma dos números")
print("3- Cubo do menor numero")

op = int(input("Informe a opção desejada: "))

if op == 1:
    media = (n1*2 + n2*3)/5
    print(f"A média ponderada é: {media}")
elif op == 2:
    quad_soma = (n1 + n2)**2
    print(f"O quadrado da soma dos números é: {quad_soma}")
elif op == 3:
    if n1 < n2:
        cubo = n1**3
        print(f"O cubo do menor número é: {cubo}")
    elif n2 < n1:
        cubo = n2**3
        print(f"O cubo do menor número é: {cubo}")
    else:
        print("Os números são iguais, tente novamente")
else:
    print("Opção inválida, tente novamente")