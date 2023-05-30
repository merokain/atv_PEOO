# Implementar um programa que leia dois valores inteiros via teclado, sendo o primeiro menor que
# o segundo, e como saída, exibir apenas os números primos do início ao fim da sequência.'''

n1 = int(input(" Digite o primeiro número: "))
n2 = int(input(" Digite o ultimo número: "))
while n1<n2:
    primo = True
    i = 2
    while i<n1:
      if n1%i == 0:
        primo = False
        break
      i += 1
    if primo:
      print(n1)
    n1 +=1