qtd = int(input('Número total de mercadorias: '))

val_tot = 0

for i in range(qtd):
    val = float(input('Valor da mercadoria {}: ' .format(i + 1)))
    val_tot += val

med = val_tot / qtd

print('O valor total é R${:.2f} e a média é R${:.2f}' .format(val_tot, med))
