# Implementar um programa que leia um valor inteiro via teclado, e como saída, exibir na tela se
# o valor é primo ou não (O número é primo quando é divisível por um e por ele mesmo).


n = int(input("Digite o valor: "))
primo = True
c = 2
while c <= n:
    if n%c==0:
        primo = False
        print( n , "não é primo")
        c += 1
        break
    if primo:
        print( n ,  "é primo")
        break