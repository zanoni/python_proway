from flask import Flask, render_template, request, redirect
from alunos_class import alunos

var_nome = 'Lista de alunos'
aluno_1 = alunos('Zanoni Neto', 'Reibnitz', 47991339311)

aluno_lista = [aluno_1]

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', nome = var_nome, lista = aluno_lista)

@app.route('/novo')
def novo():
    return render_template('novo.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    aluno_novo = alunos(nome, sobrenome, telefone)
    aluno_lista.append(aluno_novo)
    return redirect('/')

app.run()





