n1 = int(input('Número de maçãs compradas: '))

if n1 < 12:
    nf = n1 * 1.3
else : 
    nf = n1

print('Custo total da compra é R${:.2f}' .format(nf))


