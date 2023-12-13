#from django.contrib.auth.models import User # importação do módulo de usuário padrão do django
from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    login = forms.CharField(max_length=30)  # nome do campo que deve aparecer
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput()) # essa opção que faz o campo aparecer os pontinhos na senha (widget=forms.PasswordInput())

    # Se precisar pegar dois campos ao mesmo ou mais utilizo a função clean da seguinte maneira
    """def clean(self): 
            clened_data = super().clean()
            nome = cleaned_data.get('login')
            senha = cleaned_data.get('senha')

            validação"""
    def clean_login(self):
        nome = self.cleaned_data['login']

        if not(nome.isalnum()): # o comando isalnum, verifica se tem algum caractere especial / se não tiver caracter especial mostra a mensagem de erro
            raise ValidationError('O nome de usuário não pode ter caractere especial')
        return nome

