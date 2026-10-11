num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(sum)
print(sub)
print(div)

#operador de comparação

bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2

print(f"O número {num1} é maior que {num2}? {bigger}")
print(f"O número {num1} é menor que {num2}? {smaller}")
print(f"O número {num1} é igual a {num2}? {equal}")
print(f"O número {num1} é diferente de {num2}? {different}")
print(f"O número {num1} é maior ou igual a {num2}? {bigger_equal}")

#operadore de atribuição

num1 += 1
num1 -= 1
num1 *= 2
num1 /= 2
