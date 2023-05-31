# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome=str(input("Insira o nome de usuário: "))
senha=str(input("Insira a senha: "))
while nome==senha:
  print("O nome de usuário e senha não podem ser iguais")
  nome=str(input("Insira o nome de usuário: "))
  senha=str(input("Insira sua senha: "))
else:
  print("Bem vindo ao sistema,{}".format(nome))