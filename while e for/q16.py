# Dado um número inteiro de entrada do usuário de quatro dígitos, imprima se este é um palíndromo ou não. Por exemplo: 1441 é um palíndromo, 1231 não é um palíndromo.

def verificar_palindromo(numero):
    numero_str = str(numero)
    numero_invertido = numero_str[::-1]
                
    if numero_str == numero_invertido:
        return True
    else:
        return False

numero = int(input("Digite um número de quatro dígitos: "))

if verificar_palindromo(numero):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
                                            