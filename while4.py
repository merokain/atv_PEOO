# Implementar um programa que leia 10 valores inteiros via teclado, e como saída, exiba na tela o
# resultado da soma.

a = b = 0
while a < 10:
    c=int(input("Digite o valor: "))
    a += 1
    b += c
print(b)