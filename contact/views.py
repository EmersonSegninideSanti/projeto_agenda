from django.shortcuts import render
from contact.models import Contact
import django.conf

# Create your views here.

def index (request, ):
    contacts = Contact.objects.filter(show=True)
    print(django.conf.settings.DEBUG)
    return render(request, 'contact/index.html', context= {
        'contacts': contacts
    })