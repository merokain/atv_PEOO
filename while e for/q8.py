
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

cand1= 22
cand2= 13
cand3=35

vtp1=0
vtp2=0
vtp3=0
print('o numero do candidato 1 é:', cand1,'\no numero do candidato 1 é:', cand2,'\ne o número do candidato 3 é:', cand3)

votantes= int(input('insira o número de votantes: '))
votos=0
while votos<=votantes:
    vots= int(input('insira o numero do seu candidato: '))
    while vots != 22 and vots!=13 and vots !=35:
        print('número invalido, insira novamente')
        vots= int(input('insira o numero do seu candidato: '))
    else:
        if vots==22:
            vtp1+=1
        if vots==13:
            vtp2+=1
        if vots==35:
            vtp3+=1
    votos+=1
print('o candidato 1 teve',vtp1,'votos\no candidato 2 teve',vtp2,'votos\ne o candidato 3 teve',vtp3,'votos')