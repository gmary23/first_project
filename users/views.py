from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from django.contrib.auth import authenticate # vai no banco de dados e verifica os usuários
from django.contrib.auth import login as authLogin # importa o login direto do authoLogin



def login(request):

    error = False

    if request.method != "POST":
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('login')
            password = request.POST.get('senha')
            user = authenticate(username=username, password=password)

            if user:
                authLogin(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True

    context = {'form':form, 'error':error}
    return render(request, 'users/login.html', context)





