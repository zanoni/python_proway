litr = float(input('Número de litros vendidos: '))
comb = input('Combustível: A-álcool, G-gasolina : ')

if comb == 'a' or 'A':
    if litr > 20:
        total = litr * 2.9 * .95
        print('Valor a ser pago é R${:.2f}' .format(total))
    else:
        total = litr * 2.9 * .97
        print('Valor a ser pago é R${:.2f}' .format(total))
elif comb == 'g' or 'G':
    if litr > 20:
        total = litr * 3.3 * .94
        print('Valor a ser pago é R${:.2f}' .format(total))
    else:
        total = litr * 3.3 * .96
        print('Valor a ser pago é R${:.2f}' .format(total))
else :
    print('Combustível incorreto')

