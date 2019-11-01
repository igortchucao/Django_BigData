from django.db import models


class Administrador(models.Model):
    login = models.CharField(primary_key=True, max_length=45)        
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'administrador'


class Aluno(models.Model):
    login = models.CharField(primary_key=True, max_length=45)        
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=11)

    def create_aluno(self, login, nome, senha, email, telefone, cpf):
        aluno = self.create(login=login, nome= nome, senha=senha, email=email, telefone=telefone, cpf=cpf)
        return aluno

    class Meta:
        managed = False
        db_table = 'aluno'


class Area(models.Model):
    areanome = models.CharField(db_column='areaNome', primary_key=True, max_length=100)  # Field name made lowercase.
    numquestoes = models.IntegerField(db_column='numQuestoes', blank=True, null=True)  # Field name made lowercase.
    login = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='login')

    class Meta:
        managed = False
        db_table = 'area'


class Avalia(models.Model):
    loginreitor = models.ForeignKey('Proreitor', models.DO_NOTHING, db_column='loginReitor', primary_key=True)  # Field name made lowercase.
    loginprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='loginProfessor')  # Field name made lowercase.
    nota = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    comentario = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'avalia'
        unique_together = (('loginreitor', 'loginprofessor'),)


class Cadastra(models.Model):
    loginprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='loginProfessor')  # Field name made lowercase.
    idquestao = models.ForeignKey('Questao', models.DO_NOTHING, db_column='idQuestao', primary_key=True)  # Field name made lowercase.
    data = models.DateField()

    class Meta:
        managed = False
        db_table = 'cadastra'


class Proreitor(models.Model):
    loginreitor = models.CharField(db_column='loginReitor', primary_key=True, max_length=45)  # Field name made lowercase.
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'proReitor'


class Professor(models.Model):
    loginprofessor = models.CharField(db_column='loginProfessor', primary_key=True, max_length=45)  # Field name made lowercase.
    nome = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45, blank=True, null=True)
    cpf = models.CharField(max_length=11)
    especialidade = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'professor'


class Questao(models.Model):
    idquestao = models.AutoField(db_column='idQuestao', primary_key=True)  # Field name made lowercase.
    texto = models.TextField(blank=True, null=True)
    ano = models.CharField(max_length=4)
    resposta = models.CharField(max_length=1)
    diretorioimagem = models.CharField(db_column='diretorioImagem', max_length=100)  # Field name made lowercase.
    alta = models.TextField(db_column='altA', blank=True, null=True)  # Field name made lowercase.
    altb = models.TextField(db_column='altB', blank=True, null=True)  # Field name made lowercase.
    altc = models.TextField(db_column='altC', blank=True, null=True)  # Field name made lowercase.
    altd = models.TextField(db_column='altD', blank=True, null=True)  # Field name made lowercase.
    alte = models.TextField(db_column='altE', blank=True, null=True)  # Field name made lowercase.
    areanome = models.ForeignKey(Area, models.DO_NOTHING, db_column='areaNome')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'questao'