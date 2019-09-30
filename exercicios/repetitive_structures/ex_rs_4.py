n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))

while n1 < 0 or n1 > 10:
    print('Primeira nota inválida')
    n1 = int(input('Primeira nota: '))

while n1 < 0 or n2 > 10:
    print('Primeira nota inválida')
    n2 = int(input('Segunda nota: '))

res = (n1 + n2) / 2

print('A média é {:.2f}' .format(res))
