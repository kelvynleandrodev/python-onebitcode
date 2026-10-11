gameDescription = """
FIFA 23 é um jogo de Futebol criado pela EA GamesSport
que permite jogar localmente ou online com outros jogadores
"""
gameName = "FIFA"
gameVersion = " 16"

gameFull = gameName + gameVersion

line = "="

print(line * 25)
# string[início:fim] - índice começa com 0 | índice final -1

# Busque toda string a partir da primeira posição

print(gameFull[0:])
print(line * 25)

# Busque toda string até a última posição

print(gameFull[:7])
print(line * 25)

# Busque toda string da primeira até a última posição

print(gameFull[0:7])
print(line * 25)

"""
string[início:fim:passo] - índice começa com 0 | índice final -1 | 
passo - determina o incremento. Por padrão esse número é o 1
"""

#Busque toda a string de 2 em 2 caracteres.
print(gameFull[::2])

# Inverta uma string de trás pra frente
print(gameFull[::-1])

# Imprime os caracteres nos índices ímpares
print(gameFull[1::2])