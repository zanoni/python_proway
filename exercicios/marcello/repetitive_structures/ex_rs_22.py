#entrada
pop = int(input('População: '))
sal_men = 0
sal_tot = 0
sal_arr = []
fil_tot = 0

#processamento
for i in range(pop):
    fil = int(input('Número de filhos do habitante {}: ' .format(i + 1)))
    sal = float(input('Salário do habitante {}: ' .format(i + 1)))
    sal_tot += sal
    sal_arr.append(sal)
    fil_tot += fil
    if sal < 150 and sal >= 0:
        sal_men += 1
    if sal < 0:
        break
    
#maior salario
sal_arr.sort()
sal_arr.reverse()
#salario media
sal_med = sal_tot / pop
#filhos media
fil_med = fil_tot / pop
#percentual salario menor 150
sal_per = sal_men / pop * 100

#saida
print('Média do salário da população R${:.2f}\n\
    Média do número de filhos é {:.2f}\n\
    Maior salário dos habitantes é {:.2f}\n\
    Percentual de pessoas com salário menor que R$150,00 é {:.0f}%' .format(sal_med, fil_med, sal_arr[0], sal_per))
