# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Implemente um programa que exiba na tela o valor de crescimento de cada país ao ano até que país A ultrapasse ou iguale a população do país B.

populacao_A = 80000
taxa_crescimento_A = 0.03

populacao_B = 200000
taxa_crescimento_B = 0.015

ano = 0

for ano in range(1, 100):
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B

    if populacao_A >= populacao_B:
        break

print("Levou ", ano , " anos para a população de A ultrapassar ou igualar a população de B.")
print("População de A: " , populacao_A , " habitantes")
print("População de B: " , populacao_B , " habitantes")
