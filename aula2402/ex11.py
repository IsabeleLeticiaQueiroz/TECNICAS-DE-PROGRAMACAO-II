nomes = ["Luiz", "Ana", "Cristina", "Fernanda", "Maria Alice"]
sair = 1
while sair != 0:
    localizar = input("Informe um nome: ")
    for nome in nomes:
        if nome == localizar:
            print(f'Nome {nome} localizado')
            break
        else:
            print('Nome não localizado')
            break
        
    sair = int(input("Informe se deseja pesquisar(1) ou sair(0): "))
        