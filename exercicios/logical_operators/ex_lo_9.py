nome = input('Nome: ')
altu = float(input('Altura: '))
sexo = input('Sexo: "M"asculino, "F"eminino : ')

if sexo == 'm' or sexo == 'M':
    peso = altu * 72.7 - 58
    print('O peso ideal de {} é {:.2f}kg' .format(nome, peso))
elif sexo == 'f' or sexo == 'F':
    peso = altu * 62.1 - 44.7
    print('O peso ideal de {} é {:.2f}kg' .format(nome, peso))
else :
    print('Sexo incorreto')
    

