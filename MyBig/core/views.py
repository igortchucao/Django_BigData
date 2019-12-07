from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *

from sys import getsizeof

import random


from django.views.generic import ListView

from django.db.models import Q

ferramentas = []

def home(request):
    '''limProva = 20
    area = request.GET.get('areas')
    download = request.GET.get('downloads')
    question = Questao.objects.filter(areanome = area)
    question2 = question[:20]'''
    if(getsizeof(ferramentas) == 28):
        appendes = [Ferramenta("Chave de Fenda", "25/12/2009", "não há manutenção", "25/12/2019", 5, "chave_de_fenda"),
                    Ferramenta("Chave de Boca", "25/12/2009", "não há manutenção", "25/12/2019", 5, "chave_de_boca")]
        ferramentas.extend(appendes)
    return render(request, 'home.html', {'test' : ferramentas}) 

def cadastrar(request):
    if(request.GET.get):
        appendes = [Ferramenta(request.GET.get('nome'), 
                    request.GET.get('dataInser'), 
                    request.GET.get('dataManu'),
                    request.GET.get('dataRep'),
                    request.GET.get('qnt'),
                    request.GET.get('foto'))]
        ferramentas.extend(appendes)
    return render(request, 'cadastrarobjeto.html')

def dados(request):
    
    return render(request, 'dados.html')

def sobre(request):
    return render(request, 'sobre.html')