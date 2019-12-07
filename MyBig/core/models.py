from django.db import models

# CRIE AQUI AS FERRAMENTAS. BASTA MUDAR OS DADOS DO OBJETO 
class Ferramenta:
    def __init__(self, nome, data_insercao, data_manutencao, data_reposicao, qnt, foto):
        self.nome = nome
        self.data_insercao = data_insercao
        self.data_manutencao = data_manutencao
        self.data_reposicao = data_reposicao
        self.qnt = qnt
        self.foto = foto