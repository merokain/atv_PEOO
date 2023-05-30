# Implementar um programa que leia um valor inteiro via teclado, em seguida, calcule o fatorial de
# um número (O fatorial de 5! = 5 × 4 × 3 × 2 × 1 = 120), e como saída, exiba na tela o resultado.

c = int(input("Digite o valor: "))
m = 1
while c > 0:
    m = c*m
    c -= 1
print(m)