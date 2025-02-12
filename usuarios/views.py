from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if  formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'Usuario: {usuario} foi criado com sucesso!')
            return redirect('login')
    else:
        formulario = UserRegisterForm()
    return render(request, 'usuarios/registrar.html', {'formulario': formulario})

def logout_view(request):
    logout(request)  # Faz o logout do usuário
    return render(request, 'usuarios/logout.html')  # Renderiza a página de logout

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Atualiza o formulário com os dados do POST
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {user.username}!')  # Mantém a mensagem de boas-vindas
                return redirect('investimentos')  # Redireciona para a página de investimentos após o login
            else:
                messages.error(request, 'Usuário ou senha incorretos. Tente novamente.')
    return render(request, 'usuarios/login.html', {'form': form})  # Passa o formulário para o template 