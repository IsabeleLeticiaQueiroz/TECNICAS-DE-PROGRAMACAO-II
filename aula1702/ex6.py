i = int(input("Informe o indice de poluicao: "))

match i:
    case 0 | 1 | 2:
        print("Indice de poluição aceitável")
    case 3 | 4 | 5:
        print("Suspender atividades do grupo 1")
    case 6 | 7:
        print("Suspender atividades do grupo 1 e 2")
    case _:
        print("Suspender atividades de todos os grupos")
        
        