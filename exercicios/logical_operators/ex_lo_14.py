n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

val = [n1, n2, n3]

val.sort()

print('O maior valor é {:.0f}' .format(val[2]))