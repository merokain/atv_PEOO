#7) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num= int(input('insira um número: '))
if num/1==num and num/num==1:
  print('o número {} é primo'.format(num))
else:
   print('o número {} não é primo'.format(num))