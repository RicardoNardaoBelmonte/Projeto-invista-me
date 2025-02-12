"""
URL configuration for Projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from invista_me import views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url para pagina admin de administradores
    path('admin/', admin.site.urls),
    #pagina para login
    path('login/', usuario_views.login_view, name='login'),
    #pagina para logout 
    path('logout/', usuario_views.logout_view, name='logout'),
    #pagina para criar usuarios
    path('conta/', usuario_views.novo_usuario, name='novo_usuario'),
    #pagina principal investimentos
    path('',views.investimentos, name= 'investimentos'),
    #pagina para criar investimento 
    path('novo_investimento/', views.criar, name='novo_investimento'),
    #pagina para editar investimento
    path('novo_investimento/<int:id_investimento>', views.editar, name='editar'),
    #Pagina para visualizacao dos detalhes de um determinado investimento
    path('<int:id_investimento>', views.detalhe, name='detalhe'),
    #pagina para exclusao de algum determinado investimento
    path('excluir_investimento/<int:id_investimento>', views.excluir, name='excluir') 
]       
