from django.db import models

from pymongo import MongoClient
from pymongo import errors

# Create your models here.
banco = MongoClient('172.18.0.206', 27017).testetp2
'''for doc in banco.empresas.find({}):
    print(doc)'''

class Pesquisa:
    def __init__(self, text):
        self.text = text