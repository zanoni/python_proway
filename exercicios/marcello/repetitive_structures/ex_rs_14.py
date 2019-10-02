alu = int(input('Número de alunos: '))

med = 0

for i in range(alu):
    val = int(input('Nota: '))
    med += val / alu

print('A média é {:.3f}' .format(med))


