#entrada
vetor = []

#processamento
  
for i in range(5):
    vetor.append(int(input('{}º número: ' .format(i + 1))))
    
vetor.reverse()

#saida

print('Ordem inversa do vetor: {}' .format(vetor))
