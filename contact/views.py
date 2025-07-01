from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
import django.conf
from django.core.paginator import Paginator

# Create your views here.

def index (request, ):
    contacts = Contact.objects.filter(show=True)
    print(django.conf.settings.DEBUG)
    paginator = Paginator(contacts, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'contact/index.html', context= {
        'page_obj': page_obj
    })

def search(request, ):
    # Código para procurar em qualquer campo
    research_value = request.GET['q'].strip()
    if research_value == '':
        return index(request)
    print(request.GET)
    print(research_value)
    # Aqui acontece uma query. QuerySetApi - field lookup.
    contacts = Contact.objects.filter(first_name__icontains = research_value)
    paginator = Paginator(contacts, 25)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render (request,'contact/index.html', context = {
        'page_obj': page_obj
    })
    # Código simples para procurar em ids apenas.
    # research_value = request.GET['q']
    # print(request.GET)
    # print(research_value)
    # try: 
    #     research_value = int(research_value)
    # except:
    #     return index(request)
    # contacts = Contact.objects.filter(id = research_value)
    # return render(request, 'contact/index.html', context= {
    #     'contacts': contacts
    # })

def contact_view (request, id_number):
    contact = Contact.objects.filter(id=id_number).first()
    if contact is None:
        raise Http404
    
    print(django.conf.settings.DEBUG)
    return render(request, 'contact/contact.html', context= {
        'contact': contact
    })

def create (request):
    if request.method == 'POST':
        print(request.method)
        print(request.POST.get('first_name'))
        print(request.POST.get('last_name'))
    print(request.method)
    return render(request,'contact/create.html', )