gamesSet = {"Fifa 23", "Tha Last of Us Part I", "The Last of Us Part II", "GTA V", "GTA IV", 
            "Gran Turismo 7", "Forza Horizon 5", "Call of Duty WW2"}

print(gamesSet)

# 1 - Buscar o tamanho do set

print(len(gamesSet))

# 2 - True e 1 são considerados o mesmo valor

exampleSet = {"Fifa 23", True, 1, 90.50}

print(exampleSet)

# 3 - adicionar itens de outro set

gamesSet.update(exampleSet)

print(gamesSet)
# 4 - remover um item no set

gamesSet.remove(True)
gamesSet.remove(90.50)

print(gamesSet)

# Não possibilta recuperar o valor por fatiamento ou slice

