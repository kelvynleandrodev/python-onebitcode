name = input("digite o nome do jogo:\n ")
yearLauch = int(input("Digie o ano de lançamento:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planIncluded = input("Digite se o plano está incluso (True/False):\n").lower() == 'true'

print(f"Nome do Jogo: {name}")
print(f"Ano de Lançamento: {yearLauch}")
print(f"Preço do Jogo: {gamePrice}")
print(f"Plano Incluído: {planIncluded}")