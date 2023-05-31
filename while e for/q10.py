# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10,
# o valor inicial e final devem ser informados também pelo usuário


base=int(input('montar a tabuada do: '))
ti=int(input('por qual número começar a tabuada: '))
tf=int(input('em qual número terminar: '))
if tf<=ti:
  print('o primeiro termo da tabuada deve ser maior que o ultimo\ninsira novamente')
  tf=int(input('em qual número terminar: '))
else:
    for t in range(ti,(tf+1)):
        print('{} x {} ='.format(base,t), base*t)