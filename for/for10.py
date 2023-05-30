# Implementar um programa que leia um valor inteiro via teclado, que corresponde o número de
# termos de uma série de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...), e como saída, exiba na tela
# cada valor da sequência.

num_ter = int(input("Digite o numero de termos da serie Fibinacci: "))
ter_ant = 1
ter_atu = 1
print(ter_ant)
print(ter_atu)
for i in range(2 , num_ter):
    prox_ter = ter_ant + ter_atu
    print(prox_ter)
    ter_ant = ter_atu
    ter_atu = prox_ter