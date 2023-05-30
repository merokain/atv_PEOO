# Implementar um programa que leia 10 valores reais via teclado, e como saída, exiba o menor
# valor, o maior valor e a média de todos os valores.

maximo = 0
menor = 999999
soma = 0
for i in range(10):
    v = int(input("Digite um valor: "))
    maximo = max(maximo, v)
    menor = min(menor, v)
    soma += v
    m = soma/10
print("O maior valor é: " , maximo , "o menor valor é: " , menor , "e a média é: " , m )