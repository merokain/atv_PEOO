# Implementar um programa que leia 20 valores reais via teclado, e como saída, exiba na tela o
# resultado da média.

n = a = 0
while n < 20:
    val = int(input("Digite o valor: "))
    n +=1
    a +=val
print(a/20)