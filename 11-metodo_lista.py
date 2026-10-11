gamesList = ["The Last of Us Parte II", "Resident Evil 4", "Residen Evil 3", "Grand theft Auto IV"]

# 1 - Tamanho da lista 

print(len(gamesList)) #len vem da palavra length

# 2 - Recuperar item da lista pelo o índice

print(gamesList.index("Resident Evil 4"))

# 3 - adicionar item no final da lista

gamesList.append("Need for speed Most Wanted")
print(gamesList)

# 4 - Ordenar lista

gamesList.sort()
print(gamesList)

# 5 - copiar itens de uma lista para outra

gameReset = gamesList.copy()
gameReset.remove("Resident Evil 4")
print(gameReset)

# 6 - Remove todos os itens da lista

gamesList.clear()

print(gamesList)