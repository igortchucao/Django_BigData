from django.db import models

# CRIE AQUI AS FERRAMENTAS. BASTA MUDAR OS DADOS DO OBJETO 
class ChaveFenda:
    def __init__(self):
        self.nome = "Chave de Fenda"
        self.data_insercao = "25/12/2009"
        self.data_manutencao = "não há manutenção"
        self.data_reposicao = "25/12/2019"
        self.foto = "chave_de_fenda"

class ChaveBoca:
    def __init__(self):
        self.nome = "Chave de Boca"
        self.data_insercao = "25/12/2009"
        self.data_manutencao = "não há manutenção"
        self.data_reposicao = "25/12/2019"
        self.foto = "chave_de_fenda"