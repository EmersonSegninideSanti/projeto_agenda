from django.urls import path
from contact import views



urlpatterns = [
    path( '', views.index, name= 'index'),
    path( 'contact/search/', views.search , name="search"),

# CRUD do modelo Contact 
    path( 'contact/<int:id_number>/', views.contact_view, name = 'contact',),
    path( 'contact/create/', views.create, name='create',),
]