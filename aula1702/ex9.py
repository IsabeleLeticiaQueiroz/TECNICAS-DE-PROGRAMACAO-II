cat = input("Informe qual a sua categoria (a,b ou c): ")
sal = float(input("Informe o seu salário: "))

match cat:
    case "a":
        total = sal + (sal*0.1)
        print(f"O seu salario atual é: {sal}")
        print(f"O seu novo salário é: {total}")
    case "b":
        total = sal + (sal*0.15)
        print(f"O seu salario atual é: {sal}")
        print(f"O seu novo salário é: {total}")
    case "c":
        total = sal + (sal*0.25)
        print(f"O seu salario atual é: {sal}")
        print(f"O seu novo salário é: {total}")
    case _:
        print("Categoria inválida, tente novamente")
        