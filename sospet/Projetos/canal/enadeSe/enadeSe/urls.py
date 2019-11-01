"""enadeSe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('prova/', views.menu_prova),
    path('gerarprova/', views.gerar_prova, name='geraprova'),
    path('home/', views.index, name='home'),
    path('professor/', views.professor),
    path('cadastro/', views.cadastro),
    path('', views.index),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_ROOT, document_root =settings.MEDIA_ROOT)
