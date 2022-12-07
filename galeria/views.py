import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout, logout
from django.contrib import messages
from galeria.models import RegistroLogin


def index(request):
        return render(request, 'galeria/index.html')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'galeria/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
                
        return redirect('index')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'galeria/login.html')
    else:
        usernarme = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=usernarme, password=senha)

        if user:
            login(request, user)
            horario_atual = datetime.datetime.now()
            RegistroLogin.objects.create(
                user=user,
                horario_entrada=horario_atual
            )
            return redirect('index')
        else:
            return HttpResponse('Nome ou senha inválidos!')


def logoutuser(request):

    user = request.user #Vai ser pedido o usuário

    registro_login = RegistroLogin.objects.filter(user=user).first() #Vai comparar os dados do usuário registrado com o BD
    if registro_login: #Se o usuário for verdadeiro(registrado)
        horario_saida = datetime.datetime.now() #Vai ser registrado o horário que a pessoa saiu do login
        registro_login.horario_saida = horario_saida
        registro_login.save()  #É salvo a saída da pessoa

    logout(request) #É pedido e feito o logout(saída) do usuário registrado
    return redirect('index') #Em seguida, é redirecionado pra página home