# Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa
# anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de
# crescimento de 1.5%. Implemente um programa que exiba na tela o valor de crescimento de cada
# país ao ano até que país A ultrapasse ou iguale a população do país B.'''

pa = 80000
ta = 0.03
pb = 200000
tb = 0.015
ano = 0
while pa <= pb:
    print("Ano: " , ano )
    print("População do país A: " , pa )
    print("População do país B: " , pb )
    pa = pa + (pa*ta)
    pb = pb + (pb*tb)
    ano = ano + 1