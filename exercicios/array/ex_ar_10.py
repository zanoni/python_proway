#entrada
n = int(input('Quantidade de números: '))
vetor = []
aux = 0

#processamento
  
for i in range(n):
    vetor.append(float(input('{}º número: ' .format(i + 1))))

num = float(input('Insira mais um número: ' .format(i + 1)))
vetor.append(num)

for i in range(len(vetor)):
    for j in range(len(vetor)):
        if vetor[i] < vetor[j]:
            aux = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = aux

#saida

for i in range(len(vetor)):
    print('O {}° menor número do vetor é {}' .format(i + 1, vetor[i]))

