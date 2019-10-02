class alunos:
    def __init__(self, nome, sobrenome, telefone):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
    def nome_completo(self):
        nome_completo = self.nome + ' ' + self.sobrenome
        return nome_completo
