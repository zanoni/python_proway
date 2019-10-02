from flask import Flask, render_template, request
from alunos_class import alunos

var_nome = 'Lista de alunos'
aluno_1 = alunos('Zanoni', 'sdsa', 9898982)
aluno_2 = alunos('loc', 'dsda', 32874)
aluno_3 = alunos('kesaw', 'ulre', 93232)
aluno_4 = alunos('urete', 'loreas', 73261)

aluno_lista = [aluno_1, aluno_2, aluno_3, aluno_4]

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', nome = var_nome, lista = aluno_lista)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/aluno_salvar')
def salvar():
    nome = request.form('nome')
    sobrenome = request.form('sobrenome')
    telefone = request.form('telefone')  
    return 'Aluno salvo'

app.run()





