sal_in = float(input('Salário fixo: '))
val_ve = float(input('Valor das vendas: '))

if val_ve <= 1500:
    sal_fn = sal_in + val_ve * .03
else :
    sal_fn = sal_in + val_ve * .03 + (1500 - val_ve) * .05

print('O Salário total será: R${:.2f}' .format(sal_fn))    

