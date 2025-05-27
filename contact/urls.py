from django.urls import path
from contact import views



urlpatterns = [
    path( '', views.index, name= 'index'),
    path( '<int:id_number>/', views.contact_view, name = 'contact',)
]