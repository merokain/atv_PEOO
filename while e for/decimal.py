#decimal para binário
n = int(input("Informe um número em decimal: "))
res = ""

while n > 1:
    res = str(n % 2) + res
    n = n // 2

res = str(n) + res

print(res)

#binario para decimal
b = input("Informe um número binário: ")
ib = b[::-1]
#percorrer cada digito do número binário
for d in ib:
    print(d)