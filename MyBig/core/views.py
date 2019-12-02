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


def home(request):
    '''limProva = 20
    area = request.GET.get('areas')
    download = request.GET.get('downloads')
    question = Questao.objects.filter(areanome = area)
    question2 = question[:20]'''
    return render(request, 'home.html') 

def dados(request):
    return render(request, 'dados.html')

def sobre(request):
    return render(request, 'sobre.html')