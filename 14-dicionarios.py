gameFifa = {
    "nome": "Fifa 23",
    "ano de lancamento": 2022,
    "preco": 129.90,
    "avaliacao":8.4,
    "genero":["esporte", "simulador"]
    
}
print("-"*20)
print(gameFifa)
print("-"*20)
print(type(gameFifa))
print("-"*20)
print(len(gameFifa))

# Recuperar elementos do dicionário:
print("-"*20)
print(gameFifa["genero"])
print("-"*20)
print(gameFifa.get("nome"))
print("-"*20)
print(gameFifa.keys())
print("-"*20)
print(gameFifa.values())
print("-"*20)
print(gameFifa.items())
print("-"*20)
gameFifa["Jogadores"] = 2
print(gameFifa)
print("-"*20)
gameFifa.update({"Jogadores":1})
print(gameFifa)
print("-"*20)
# 7 - Removendo item no dicionário
gameFifa.pop("Jogadores")
print(gameFifa)

