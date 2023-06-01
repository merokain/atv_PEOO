''' Escreva um algoritmo que retorne a seguinte figura. Por exemplo: x = 3

    3
   3 3
  3 3 3
   3 3
    3'''

def imprimir_figura(x):
    for i in range(x, 0, -1):
        linha = " " * (i - 1)
        for j in range(x - i + 1):
            linha += str(x) + " "
        print(linha[:-1])
    for i in range(2, x + 1):
        linha = " " * (i - 1)
        for j in range(x - i + 1):
            linha += str(x) + " "
        print(linha[:-1])

x = 3
imprimir_figura(x)
                                                                            
