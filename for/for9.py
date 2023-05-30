# Implementar um programa que leia um valor inteiro via teclado, em seguida, calcule o fatorial de
# um número (O fatorial de 5! = 5 × 4 × 3 × 2 × 1 = 120), e como saída, exiba na tela o resultado.'''

num = int(input("Digite um numero inteiro: "))
f = 1
for i in range (1, num + 1):
    f *= i
print("O fatorial de", num , "é: ", f)