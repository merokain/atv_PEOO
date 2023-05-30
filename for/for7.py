# Implementar um programa que leia 15 valores inteiros via teclado, e como saída, exiba na tela o
# maior valor.

maior = 0
for i in range(15):
    v = int(input("Digite um valor: "))
    maior = max(maior, v)
print("O maior valor é: " , maior )