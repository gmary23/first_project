
from django.urls import path
from django import views
from django.contrib.auth import views as auth_views # views de autenticação

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]