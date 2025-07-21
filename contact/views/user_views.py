from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

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

def user_update(request, user_id):
    user = get_object_or_404(User, user_id)
    form = RegisterForm(instance=user)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
    render(request,'contact/register.html',context={
        'form': form,
    })