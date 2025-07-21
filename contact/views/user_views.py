from django.shortcuts import render
from contact.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = RegisterForm()
    return render(
        request, 'contact/register.html', context={
            'form': form
        }
    )