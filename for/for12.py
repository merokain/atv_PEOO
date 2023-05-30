# Implementar um programa que leia dois valores inteiros via teclado, sendo o primeiro menor que o segundo, e como saída, exibir apenas os números primos do início ao fim da sequência.

valor1 = int(input("Digite o primeiro valor inteiro: "))
valor2 = int(input("Digite o segundo valor inteiro: "))

print("Números primos entre ", valor1 , "e " , valor2, ":")
for numero in range(valor1, valor2 + 1):
    if numero < 2:
        continue

    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print(numero)
