#entrada
dias = int(input('Quantidade de dias: '))
temp = []
temp_maior = -999999
temp_menor = 999999
dias_inf = 0

#processamento
  
for i in range(dias):
    temp.append(float(input('Temperatura do {}º: ' .format(i + 1))))

for i in range(len(temp)):
    if temp[i] > temp_maior:
        temp_maior = temp[i]    

for i in range(len(temp)):
    if temp[i] < temp_menor:
        temp_menor = temp[i]    

temp_med = sum(temp) / dias

for n in temp:
    if n < temp_med:
        dias_inf += 1

#saida

print('a) Menor temperatura do ano é {:.2f}°\n\
b) Maior temperatura do ano é {:.2f}°\n\
c) Temperatura média anual é {:.2f}°\n\
d) {:.0f} dias tiveram a temperatura inferior à média anual' .format(temp_menor, temp_maior, temp_med, dias_inf))

