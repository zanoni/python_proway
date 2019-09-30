'''

n = [4, 7, 2, 3]
maior =0
for i in range(len(n)):
    if n[i]> maior:
        maior = n[i]

print(maior)

'''

#entrada
qtd_pos = int(input('Quantidade de posições: '))
q = []
num_menor = 0

#processamento
while len(q) < qtd_pos:
    num = float(input('Número: '))
    if num >= 0:
        q.append(num)
    else:
        print('O número tem que ser positivo')
    
for i in range(len(q)):
    if q[i] < num_menor:
        num_menor = q[i]

#saida

print('O menor número é {} e está na posição {}' .format(num_menor, q.index(num_menor)))
