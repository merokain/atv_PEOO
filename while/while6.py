# Implementar um programa que leia 15 valores inteiros via teclado, e como saída, exiba na tela o
# menor valor.'''

n = 0
menor = 99999
while n < 15:
    val = int(input("Digite o valor: "))
    menor = min(menor, valor)
    n += 1
print("O menor valor é: " , menor )