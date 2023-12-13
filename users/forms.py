from django.contrib.auth.models import User # importação do módulo de usuário padrão do django
from django import forms

class LoginForm(forms.ModelForm):
    class Meta: 
        model = User
        fields = ['username', 'password']
        labels = {'username':'Login', 'password':'Senha'}
