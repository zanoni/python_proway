#entrada

alun_qtd = int(input('Quantidade de alunos: '))
nota_qtd = int(input('Quantidade de notas: '))

#processamento

soma_tot = 0
for aluno in range(alun_qtd):
    for nota in range(nota_qtd):
        soma_nota = float(input('Aluno {} => {}' .format(aluno, nota))
        soma_tot += soma_nota

nota_med = soma_tot / (alun_qtd * nota_qtd)

print('Média geral é {}' .format(nota_med))

#saida


