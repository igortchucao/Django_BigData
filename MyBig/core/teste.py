from pymongo import MongoClient
from pymongo import errors

# Create your models here.
banco = MongoClient('172.18.0.206', 27017).testetp2
print('banco conectado com sucesso!')

for doc in banco.empresas.find({}):
    print(doc)