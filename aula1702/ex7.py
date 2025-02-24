print("*********CALCULO DE GRANDEZAS ELÉTRICAS*********")
print("1- Tensao (em Volts)")
print("2- Resistencia (em Ohms)")
print("3- Corrente (em Amperes)")

n = int(input("Informe a grandeza desejada: "))

match n:
    case 1:
        r = float(input("Informe a resistência (em Ohms): "))
        i = float(input("Informe a corrente (em Amperes): "))
        u = r*i
        print(f"A tensão é de {u} Volts")
    case 2:
        u = float(input("Informe a tensão (em Volts): "))
        i = float(input("Informe a corrente (em Amperes): "))
        r = u/i
        print(f"A resistência é de {r} Ohms")
    case 3:
        u = float(input("Informe a tensão (em Volts): "))
        r = float(input("Informe a resistência (em Ohms): "))
        i = u/r
        print(f"A corrente é de {i} Amperes")
    case _:
        print("Opção inválida, tente novamente")