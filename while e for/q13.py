''' Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.'''


tabela_candidatos = {
    1: "José",
    2: "João",
    3: "Maria",
    4: "Ana"
}

votos_candidatos = {candidato: 0 for candidato in tabela_candidatos}
votos_nulos = 0
votos_brancos = 0
total_votos = 0

while True:
    voto = int(input("Informe o código do candidato (ou 0 para encerrar): "))
                        
    if voto == 0:
        break
                                        
    if voto in tabela_candidatos:
        votos_candidatos[voto] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
                                                                
    total_votos += 1

                                                                        
print("\nResultados da Eleição")
print("---------------------")

for candidato, nome in tabela_candidatos.items():
    print(f"Total de votos para {nome}: {votos_candidatos[candidato]}")
    
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_brancos}")

percentagem_nulos = (votos_nulos / total_votos) * 100
percentagem_brancos = (votos_brancos / total_votos) * 100

print(f"Percentagem de votos nulos sobre o total de votos: {percentagem_nulos:.2f}%")
print(f"Percentagem de votos em branco sobre o total de votos: {percentagem_brancos:.2f}%")
