carros = int(input('Número de carros vendidos: '))
val_total = int(input('Valor total de vendas: '))
sal = int(input('Salário fixo: '))
por_carro = int(input('Valor por carro vendido: '))

sal_fn = sal + val_total * .05 + carros * por_carro

print('Salário final é {}' .format(sal_fn))
