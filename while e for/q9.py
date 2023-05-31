# Faça um programa que calcule o número médio de alunos por turma.
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
# As turmas não podem ter mais de 40 alunos.
soma=turmalun=0
quantturms= int(input('informe a quantidade de turmas: '))
if quantturms>10:
  print('a escola não pode ter mais e 10 turmas\n insira novamente')
  quantturms= int(input('informe a quantidade de turmas: '))
else:
    while quantturms>turmalun:
        turmalun+=1
        quantalunos= int(input('Informe a quantidade de alunos da {}° turma: '.format(turmalun)))
        if quantalunos>40:
            print('a turma não pode ter mais de quarenta alunos\n insira novamente')
            quant= int(input('Informe a quantidade de alunos: '))
        soma+=quantalunos
med=soma/quantturms
print('a média de alunos por sala é de', round(med))