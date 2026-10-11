# Substituindo caractere repetido
"""
Escreva um programa Python para obter uma string de
uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', 
exceto o próprio primeiro caractere
"""
# Ex:

# # fifa 23 → fi#a 23

minha_palavra = "concentração"

#passo1

indice_palavra = minha_palavra[0]

print(f"A primeira letra da sua string é {indice_palavra}")

#passo2

partea = minha_palavra[0:1]

print(partea)

parteb = minha_palavra[1:]

print(parteb)

parteb_modificada = parteb.replace(indice_palavra, "$")

print(parteb_modificada)

palavra_final = partea + parteb_modificada

print(palavra_final)




