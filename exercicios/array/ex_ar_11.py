#entrada
n = int(input('Quantidade de números: '))
vetor = []

#processamento
  
for i in range(n):
    vetor.append(float(input('{}º número: ' .format(i + 1))))

num = float(input('Número: '))

if num in vetor:
    vetor.remove(num)

#saida

print('Vetor: {}' .format(vetor))

