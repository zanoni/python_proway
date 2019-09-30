sala = int(input('Salário atual: '))
perc = int(input('Percentual de reajuste: '))

sala_fn = sala + sala * perc / 100

print('Novo salário é {}' .format(sala_fn))
