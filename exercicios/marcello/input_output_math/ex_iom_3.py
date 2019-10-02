anos = int(input('Quantidade de anos: '))
meses = int(input('Quantidade de meses: '))
dias = int(input('Quantidade de dias: '))

dias_fn = anos * 365 + meses * 30 + dias

print('A sua idade em dias é: {}' .format(dias_fn))