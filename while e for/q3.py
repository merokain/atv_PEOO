
# Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome=str(input("Digite seu nome: "))
while len(nome)<=3:
  print("O nome deve conter mais de três caracteres.")
  nome=str(input("Insira seu nome novamente: "))
else:
    idade=int(input("Insira sua idade: "))
    while id <=0 or id>150:
        print("A idade deve estar entre 0 e 150.")
        idade=int(input("Insira sua idade novamente: "))
    else:
        salario=int(input("Insira seu salário: "))
        while salario<=0:
            print("O salário deve ser maior que 0.")
            salario=int(input("Insira seu salário: "))
        else:
            sexo=str(input("Insira seu sexo: "))
            sexo.lower()
            while sexo!='feminino' and sex!='masculino':
                print("Sexo inválido.")
                sexo=str(input("Insira seu sexo: "))
            else:
                ec=str(input("Insira seu estado civil: "))
                ec.lower()   
                while ec[0:1]!='s' and ec[0:1]!='c' and ec[0:1]!='v' and ec[0:1]!='d' :
                    print("Insira estado civíl válido.")
                    ec=str(input("Insira seu estado civil: "))
                else:
                    print("Informações válidas.")