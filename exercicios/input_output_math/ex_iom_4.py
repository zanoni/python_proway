total = int(input('Quantidade total de votos: '))
branc = int(input('Quantidade de votos brancos: '))
nulos = int(input('Quantidade de votos nulos: '))
valid = int(input('Quantidade de votos válidos: '))

branc_perc = 100 * branc / total
nulos_perc = 100 * nulos / total
valid_perc = 100 * valid / total

print('Percentual de votos em braco é {}%\nPercentual de nulos é {}%\nPercentual de válidos é {}%' .format(branc_perc, nulos_perc, valid_perc))
