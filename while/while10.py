# Implementar um programa que leia um valor inteiro via teclado, que corresponde o número de
# termos de uma série de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...), e como saída, exiba na tela
# cada valor da sequência.

q = int(input("Quantidade de termos: "))
t1 = 1
t2 = 2
print(f'{t1}, {t2}', end=" ")
c = 3
while c <= q:
    t3 = t1+t2
    print(f', {t3}', end=' ')
    t1=t2
    t2=t3
    c += 1