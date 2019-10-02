time_1 = input('Time 1: ')
time_2 = input('Time 2: ')
gol_1 = int(input('Quantos gols o time {} fez: ' .format(time_1)))
gol_2 = int(input('Quantos gols o time {} fez: ' .format(time_2)))


if gol_1 > gol_2:
    print('{} é vencedor' .format(time_1)) 

if gol_2 > gol_1:
    print('{} é vencedor' .format(time_2))   

if gol_1 == gol_2:
    print('Empate')   
