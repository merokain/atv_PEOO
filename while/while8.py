# Implementar um programa que leia 10 valores reais via teclado, e como saída, exiba o menor
# valor, o maior valor e a média de todos os valores.''

n = valor = 0
maximo = 0
menor = 999999
while n < 10:
    v = int(input("Digite o valor: "))
    maximo = max(maximo, v)
    menor = min(menor, v)
    m = (valor + v)/2
    n += 1
print("O maior valor é: ", maximo , "O menor valor é: ", menor , "e a média é: ", m)