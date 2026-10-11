gamesTuple = ("Fifa 23", "GTA V", "Gran Turismo 7", "Minecraft", "Need for speed")

print(gamesTuple)
print(type(gamesTuple))

#Não é possível adicionar ou remover valores  em  uma tupla. Além disso também nãao é possível ordenar os valores

# 1 - Buscar os dois primeiros itens da dupla

print(gamesTuple[:2])

# 2 - Buscar o último item da lista

print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada possição

print(gamesTuple[:3])

# 4 - Buscar jogos de uma posiçãao em diante

print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo o indice

try:
    print(gamesTuple.index("Gran Turismo"))
except ValueError:
    print("Jogo não encontrado na tupla.")