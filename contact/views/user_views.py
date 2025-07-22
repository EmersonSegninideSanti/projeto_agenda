from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request,'Criação de usuário bem sucedida.')
            return redirect('index')

    else:
        form = RegisterForm()
    return render(
        request, 'contact/register.html', context={
            'form': form,
        }
    )

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            auth.login(request,user)
            messages.success(request,'Login bem sucedido.')
            redirect('index')
    form = AuthenticationForm(request)
    # user = form.get_user()
    return render(
        request, 'contact/login.html', context= {
            'form': form,
            # 'user': user,
        }
    )

def user_logout(request):
    auth.logout(request)
    return redirect('login')

def user_update(request, user_id):
    user = get_object_or_404(User, user_id)
    form = RegisterForm(instance=user)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
    render(request,'contact/register.html',context={
        'form': form,
    })