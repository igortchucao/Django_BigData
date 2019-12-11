from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .models import banco as b

from sys import getsizeof

import random


from django.views.generic import ListView

from django.db.models import Q


def home(request):
    '''limProva = 20
    area = request.GET.get('areas')
    download = request.GET.get('downloads')
    question = Questao.objects.filter(areanome = area)
    question2 = question[:20]'''

    numEmpresas = 0
    for e in banco.empresas.find():
        numEmpresas += 1
    for e in banco.empresasProteste.find():
        numEmpresas += 1

    numComentarios = 0
    for e in banco.empresas.find():
        if "comentarios" in e.keys():
            numComentarios += len(e['comentarios'])
    for e in banco.empresasProteste.find():
        if "comentarios" in e.keys():
            numComentarios += len(e['comentarios'])

    a = [x for x in banco.empresas.find()]
    b = [x for x in banco.empresasProteste.find()]
    top10 = sorted((a+b), key=lambda i: i['nota'], reverse=True)[:10].copy()

    a = [x for x in banco.empresas.find() if x["nota"] > 0]
    b = [x for x in banco.empresasProteste.find() if x["nota"] > 0]
    top10p = sorted((a+b), key=lambda i: i['nota'], reverse=False)[:10].copy()

    a = [x for x in banco.empresas.find()]
    b = [x for x in banco.empresasProteste.find()]
    top10r = sorted((a+b), key=lambda i: i['numReclamacoes'], reverse=True)[:10].copy()

    a = [x for x in banco.empresas.find() if x["tempoRespostaI"] > 0]
    b = [x for x in banco.empresasProteste.find() if x["tempoRespostaI"] > 0]
    top10trM = sorted((a+b), key=lambda i: i['tempoRespostaI'], reverse=False)[:10].copy()

    a = [x for x in banco.empresas.find()]
    b = [x for x in banco.empresasProteste.find()]
    top10tr = sorted((a+b), key=lambda i: i['tempoRespostaI'], reverse=True)[:10].copy()

    return render(request, 'home.html', {'numEmpresas' : numEmpresas, 'numComentarios' : numComentarios, 'top10' : top10 , 'top10p' : top10p, 'top10r' : top10r, 'top10tr' : top10tr, 'top10trM' : top10trM}) 

def dados(request):
    p = None
    categorias = []

    for e in banco.empresas.find():
        for c in e["categorias"]:
            if c not in categorias:
                categorias.append(c)
                
    for e in banco.empresasProteste.find():
        for c in e["categorias"]:
            if c not in categorias:
                categorias.append(c)

    if(request.GET):
        if(request.GET.get('pesquisa') != None): 
            p = banco.empresas.find_one({'nome' :  request.GET.get('pesquisa')})
            return render(request, 'dados.html', {'test': p, 'categorias' : categorias})

        elif(request.GET.get('pesquisaArea') != None):
            area = request.GET.get('pesquisaArea') 
            a = [x for x in banco.empresas.find({"categorias": area})]
            b = [x for x in banco.empresasProteste.find({"categorias": area})]
            top10categ = sorted((a+b), key=lambda i: i['nota'], reverse=True)
            top10categ = top10categ[:10]

            top10categr = sorted((a+b), key=lambda i: i['numReclamacoes'], reverse=True)[:10].copy()

            count = 0
            for e in (a+b):
                if "comentarios" in e.keys():
                    count += len(e["comentarios"])

            return render(request, 'dadosArea.html', {'totalComentarios': count, 'test': p, 'categorias' : categorias, 'area' : area, 'top10' : top10categ, 'top10r' : top10categr})

    return render(request, 'dados.html', {'test': p, 'categorias' : categorias})

def sobre(request):
    return render(request, 'sobre.html')