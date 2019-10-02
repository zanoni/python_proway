n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while n2 == 0:
    n2 = int(input('Segundo valor: '))

res = n1 / n2

print('Resultado é {}' .format(res))
