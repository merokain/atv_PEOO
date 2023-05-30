# Implementar um programa que leia 20 valores reais via teclado, e como saída, exiba na tela o
# resultado da média.'''

soma = 0
for i in range(10):
    valor = int(input("Digite um valor: "))
    soma += valor
    m = soma/10
print("O valor da média é:", m)