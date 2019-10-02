#entrada
nota = []
vez = 0
alun_aci = 0

#processamento
for i in range(10):
    nota.append(float(input('Nota aluno {}: ' .format(i + 1))))
    vez += 1

nota_med = sum(nota) / vez

for n in nota:
    if n > nota_med:
        alun_aci += 1

#saida

print('Média da turma é {}\n{} alunos obtiveram nota acima desta média' .format(nota_med, alun_aci))


