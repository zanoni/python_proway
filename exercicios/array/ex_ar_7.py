#entrada
n = int(input('Tamanho dos vetores: '))
a = []
b = []
soma = []

#processamento
  
for i in range(n):
    a.append(int(input('{}º número do vetor A: ' .format(i + 1))))

for i in range(n):
    b.append(int(input('{}º número do vetor B: ' .format(i + 1))))

for i in range(len(a)):
    res = a[i] + b[i]
    soma.append(res)

#saida

print('Vetor Soma: {}' .format(soma))
