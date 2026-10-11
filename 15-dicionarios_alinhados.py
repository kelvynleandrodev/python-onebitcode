import pprint


gamesDict = {
    "resident evil 4":{
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["ação", "aventura"]
    },
    "The last of Us part II":{
        "yearLaunch": 2020,
        "classification": 9.9,
        "genre": ["ação", "aventura"]
    },
    "Grand Theft Auto V":{
        "yearLaunch": 2013,
        "classification": 10.0,
        "genre": ["ação", "aventura"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informações dentro do dicionário

print(gamesDict["Grand Theft Auto V"]["genre"])

print("-"*25)

# 2 - adicionar um ityem de um dicionnario anilhado

gamesDict["Grand Theft Auto V"]["players"] = 1

print(gamesDict["Grand Theft Auto V"])


# 3 - Excluir um dicionário
print("-"*25)


del gamesDict["resident evil 4"]

pp.pprint(gamesDict)