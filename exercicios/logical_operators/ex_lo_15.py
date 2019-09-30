n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

val = [n1, n2, n3]

val.sort()

soma = val[2] + val[1]

print('O soma dos dois maiores valores é {:.0f}' .format(soma))