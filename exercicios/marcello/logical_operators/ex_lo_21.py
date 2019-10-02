kilo = float(input('Kilos comprados: '))
frut = input('Fruta: A-morango, B-maçã : ')

if frut == 'a' or 'A':
    if kilo > 5:
        res = kilo * 2.2
    else:
        res = kilo * 2.5
elif frut == 'b' or 'B':
    if kilo > 5:
        res = kilo * 1.5
    else:
        res = kilo * 1.8
else :
    print('Fruta incorreta')

if kilo > 8 or res > 25:
    total = res * .9
else :
    total = res

print('O cliente pagará R${:.2f}' .format(total))
