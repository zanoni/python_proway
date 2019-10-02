vez = 0
val_tot = 0
rep = 's'

while rep == 's' or rep == 'S':
    vez += 1
    val = float(input('Valor da mercadoria {}: ' .format(vez)))
    rep = input('Mais mercadorias, S-sim ou N-não: ')
    val_tot += val

med = val_tot / vez

print('O valor total é R${:.2f} e a média é R${:.2f}' .format(val_tot, med))
