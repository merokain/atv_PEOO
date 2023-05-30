# Implementar um programa que leia 10 valores inteiros via teclado, e como saída, exiba na tela o
# resultado da soma.

soma = 0
for i in range(10):
    valor = int(input("Digite um valor: "))
    soma += valor
print("A soma dos valores é:", soma)