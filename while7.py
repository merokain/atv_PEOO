# Implementar um programa que leia 15 valores inteiros via teclado, e como saída, exiba na tela o
# maior valor.'''

n = 0
maximo = 0
while n < 15:
    val = int(input("Digite o valor: "))
    maximo = max(maximo, val)
    n += 1
print("O maior valor é: " , maximo)