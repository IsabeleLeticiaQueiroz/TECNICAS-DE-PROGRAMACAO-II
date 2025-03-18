print("Panificadora Pao de ontem - Tabela de precos")
for i in range(1,51):
    if i %2 == 0:
        continue
    print(f"{i} - R$ {i*0.54:.2f}")
print("Fim da tabela")
