produtos = []
for i in range(1,100):
    produto = input(f"Digite o valor do {i}° produto: ")
    produtos.append(produto)
    if produto == '0':
        break
print(f'***Voce incluiu {len(produtos)-1} produtos a compra***')
print('Os produtos in foram: ')
for produto in produtos:
    if produto == '0':
        break
    print(produto)
    
    # rever e refazer
    