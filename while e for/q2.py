# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome=str(input('insira o nom de usuário: '))
senha=str(input('insira sua senha: '))
while nome==senha:
  print('o nome de usuário e senha não podem ser iguais')
  nome=str(input('insira o nom de usuário: '))
  senha=str(input('insira sua senha: '))
else:
  print('Bem vindo ao sistema,{}!'.format(nome))