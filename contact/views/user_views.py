from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import RegisterForm, UpdateRegisterForm
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

def user_update(request,):
    if request.method != 'POST':
        form = UpdateRegisterForm(instance=request.user)
        return render(request,'contact/user_update.html',context={
            'form': form,
        })
    form = UpdateRegisterForm(data=request.POST,instance=request.user)
    if not form.is_valid():
        return render(request,'contact/user_update.html',context={
            'form': form,
        })
    form.save()
    return redirect('index')
