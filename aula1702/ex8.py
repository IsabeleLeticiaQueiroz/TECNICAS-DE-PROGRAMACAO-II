val = float(input("Informe o valor da compra:"))
f = int(input("Informe a forma de pagamento: 1 - à vista, 2 - cartão de debito, 3 - cartão de credito:"))

match f:
    case 1:
        total = val - (val*0.15)
        print(f"O valor final da compra é: {total}")
    case 2:
        total = val - (val*0.1)
        print(f"O valor final da compra é: {total}")
    case 3:
        total = val + (val*0.05)
        print(f"O valor final da compra é: {total}")
    case _:
        print("Opção inválida, tente novamente")
        