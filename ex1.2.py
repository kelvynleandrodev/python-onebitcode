# Média de 4 notas
# Escreva um programa em Python que leia quatro números e calcule a média entre esses números

num1 = int(input("Digite o a primeira nota: \n"))
num2 = int(input("Digite o a segunda nota: \n"))
num3 = int(input("Digite o a terceira nota: \n"))
num4 = int(input("Digite o a quarta nota: \n"))

soma = num1 + num2 + num3 + num4

media = soma/4

print(f"A média das quatro notas inseridas foi: {media}")

if media >=6:
    print("Foi aprovado")
else:
    print("Repetente")