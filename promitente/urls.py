"""promitente URL Configuration

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home1'),
    path('home/', views.home, name='home'),
    path('cadastrar-cliente/', views.cadastrar_cliente, name='cadastrar-cliente'),
    path('pesquisar-clientes/', views.pesquisar_clientes, name='pesquisar-clientes'),
    path('atualizar-cadastro/<int:cpf>/', views.atualizar_cadastro, name='atualizar-cadastro'),
    path('excluir-cliente/<int:cpf>/', views.excluir_cliente, name='excluir-cliente'),
    path('enviar-mensagem/<int:cpf>/', views.enviar_mensagem, name='enviar-mensagem')
]
