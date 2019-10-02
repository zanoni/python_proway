h1 = int(input('Hora de início: '))
h2 = int(input('Hora de fim: '))

if h1 < h2:
    hf = h2 - h1
else : 
    hf = 24 - h1 + h2

print('O jogo durou {}' .format(hf))
