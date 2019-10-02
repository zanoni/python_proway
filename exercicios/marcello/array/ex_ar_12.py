#entrada
n = int(input('Quantidade de números: '))
v1 = []
v2 = []
vez = 0

#processamento
  
for i in range(n):
    v1.append(float(input('{}º número do vetor V1: ' .format(i + 1))))

for i in range(n):
    v2.append(float(input('{}º número do vetor V2: ' .format(i + 1))))

for i in range(n):
    if v1[i] == v2[i]:
        vez += 1

#saida

print('Os vetores possuem {} vezes os mesmos números nas mesmas posições' .format(vez))

