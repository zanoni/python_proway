n = int(input('Valor N, tem que ser maior que 0: '))

while n <= 0:
    n = int(input('Valor N inválido: '))

for i in range(0, n):
    print(i + 1)
