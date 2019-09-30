qtd = int(input('Quantidade atual em estoque: '))
qtd_max = int(input('Quantidade máxima em estoque: '))
qtd_min = int(input('Quantidade mínima em estoque: '))

qtd_med = (qtd_max + qtd_min) / 2

if qtd >= qtd_med:
    print('Não efetuar compra')    
else :
    print('Efetuar compra')    


