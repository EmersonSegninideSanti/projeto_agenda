from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
import django.conf

# Create your views here.

def index (request, ):
    contacts = Contact.objects.filter(show=True)
    print(django.conf.settings.DEBUG)
    return render(request, 'contact/index.html', context= {
        'contacts': contacts
    })

def contact_view (request, id_number):
    contact = Contact.objects.filter(id=id_number).first()
    if contact is None:
        raise Http404
    
    print(django.conf.settings.DEBUG)
    return render(request, 'contact/contact.html', context= {
        'contact': contact
    })