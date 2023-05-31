# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base=int(input("informe a base: "))
expo=int(input("informe o expoente: "))
pot=1
count=1
while count <= expo:
  pot*= base
  count+=1

print(base,"^",expo,"=",pot)