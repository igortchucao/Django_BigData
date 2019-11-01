from django.contrib import admin
from .models import Questao

admin.site.site_header = 'Página do Administrador - ENADEsE'

# Register your models here.
@admin.register(Questao)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['idquestao', 'texto']