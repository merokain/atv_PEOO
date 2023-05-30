# Implementar um programa que leia 15 valores inteiros via teclado, e como saída, exiba na tela o
# menor valor.

menor= 9999999
for i in range(15):
    v = int(input("Digite um valor: "))
    menor = min(menor, v)
print("O menor valor é: " , menor )