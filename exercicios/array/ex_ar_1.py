#entrada
nome_arr = []

#processamento
for i in range(2):
    nome = input('Nome: ')
    nome_arr.append(nome)

nome_enc = input('Nome para encontrar: ')

if nome_enc in nome_arr:
    print('Achei')
else:
    print('Não achei')

#saida

