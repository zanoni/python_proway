print('=' * 100)
################
#entrada

sal = float(input('{}Salário líquido: ' .format(' ' * 5)))

#processamento

#saida

print('{}R${:.2f} para gastos' .format(' ' * 5, sal * .5))
print('{}R${:.2f} para investimentos a longo prazo' .format(' ' * 5, sal * .2))
print('{}R${:.2f} para investimentos a curto prazo' .format(' ' * 5, sal * .1))
print('{}R${:.2f} para livre gastos' .format(' ' * 5, sal * .2))

################
print('=' * 100)
