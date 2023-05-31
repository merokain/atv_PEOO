# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.

n=1
soma=imp=par=0
while n<11:
  num=int(input('insira o {}° número: '.format(n)))
  if num%2==0:
    par+=1
  else:
    imp+=1
  soma+=num
  n+=1
print('você informou {}° numeros ímpares'.format(imp))
print('você informou {}° numeros pares'.format(par))
print('o resultado da soma dos números que você informou é {}'.format(soma))