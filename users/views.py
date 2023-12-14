from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm #módulo que cria usuários


def logout_view(request):
    logout(request) # faz logout do usuário
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm() # exige o formulário de cadastro em branco
    else:
        form = UserCreationForm(data=request.POST) # envia para dentro do usuário padrão do django
        # Processa o formulário preenchido
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1']) # cria os login e senha
            login(request, authenticated_user) #loga no sistema
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}   
    return render(request, 'users/register.html', context)
    





