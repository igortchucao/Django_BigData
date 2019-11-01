from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from sys import getsizeof
import random
import mysql.connector as mysql

from django.views.generic import ListView
from django.db.models import Q


# Create your views here.
def login_user(request):
    return render(request, 'login.html')

def cadastro(request):
    nome = request.GET.get('inputName')
    login = request.GET.get('inputLogin')
    senha = request.GET.get('inputPassword')
    email = request.GET.get('inputEmail')
    telefone = request.GET.get('inputPhone')
    cpf = request.GET.get('inputCPF')

    if request.GET:
        aluno = Aluno.objects.create()
        aluno.nome = nome
        aluno.login = login
        aluno.senha = senha
        aluno.email = email
        aluno.telefone = telefone
        aluno.cpf = cpf
        aluno.save()

    return render(request, 'cadastro.html')

def index(request):
    return render(request, 'index.html')

class GeraProvaView(ListView):
    model = Questao
    template_name = 'prova.html'
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get('areas')
        object_list = Questao.objects.filter(areanome = query)
        return object_list

def gerar_prova(request):
    limProva = 20
    area = request.GET.get('areas')
    download = request.GET.get('downloads')
    question = Questao.objects.filter(areanome = area)
    question2 = question[:20]
    return render(request, 'prova.html', {'question':question2})

def professor(request):
    return render(request, 'professor.html')

def menu_prova(request):
    area = request.GET.get('areas')
    download = request.GET.get('downloads')
    area = Area.objects.all()
    return render(request, 'menuprova.html', {'areas':area})

def logout_user(request):
    logout(request)
    return redirect('/login/')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Aluno.objects.filter(login=username, senha=password)
        if len(user) == 1:
            return redirect('/home/')
        else:
            messages.error(request, 'Usuario e Senha inválidos.')
    return redirect('/login/')