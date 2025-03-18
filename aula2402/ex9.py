nomes = ["Maria","Joao","Paulo","Magali", "Ana"]
localizar = input("Digite o nome que deseja localizar: ")

for n in nomes:
    if n == localizar:
        print(f'Nome {n} localizado')
        break
    else:
        print('Nome não localizado')
