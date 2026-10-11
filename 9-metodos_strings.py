gameDescription = """
FIFA 23 é um jogo de Futebol criado pela EA GamesSport
que permite jogar localmente ou online com outros jogadores
"""
gameName = "Fifa16"

print(gameName.upper()) #texto todo em maisculo
print(gameName.lower()) #texto todo em minusculo
print(gameName.capitalize()) #primeira letra do texto em maiscula
print(gameName.title()) #primeira letra do texto em maiscula
print(gameName.center(10, "-")) #Centraliza um string com um caractere de preenchimento
print(gameName.find("i")) #Encontra a posição de uum determinado caractere dentro de uma string
print(gameDescription.count("F")) #Conta o número de determinados caracteres dentro de uma string
print(gameDescription.replace("FIFA", "PES")) #altera elementos
print(gameDescription.split(",")) 