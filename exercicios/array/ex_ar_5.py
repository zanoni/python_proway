#entrada
a = []
m = []

#processamento
  
for i in range(10):
    num = int(input('{}º número: ' .format(i + 1)))
    a.append(num)
    
x = int(input('Variável X: ' .format(i + 1)))

for i in range(len(a)):
    res = x * a[i]
    m.append(res)

#saida

print('Vetor M: {}' .format(m))
