#entrada
n = int(input('Quantidade de números: '))
vetor = []
aux = 0

#processamento
  
for i in range(n):
    vetor.append(float(input('{}º número: ' .format(i + 1))))

for i in range(n):
    for j in range(n):
        if vetor[i] < vetor[j]:
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux

#saida

for i in range(n):
    print('O {}° menor número do vetor é {}' .format(i + 1, vetor[i]))

