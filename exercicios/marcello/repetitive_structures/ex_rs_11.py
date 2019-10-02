n1 = int(input('Valor: '))

num = 1

for i in range(n1, n1 * 11, n1):
    print('{} X {} = {}' .format(n1, num, i))
    num += 1
