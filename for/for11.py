# Implementar um programa que leia um valor inteiro via teclado, e como saída, exibir na tela se o valor é primo ou não (O número é primo quando é divisível por um e por ele mesmo).

numero = int(input("Digite um número inteiro: "))

if numero < 2:
    print(f"O número {numero} não é primo.")
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("O número " , numero , " não é primo.")
    else:
        print("O número " , numero , " não é primo.")