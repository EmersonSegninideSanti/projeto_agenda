from django.urls import path
from contact import views


urlpatterns = [
    path( '', views.index, name= 'index'),
    path( 'contact/search/', views.search , name="search"),

# CRUD do modelo Contact 
    path( 'contact/<int:id_number>/', views.contact_view, name = 'contact',),
    path( 'contact/create/', views.create, name='create',),
    path( 'contact/<int:contact_id>/update/', views.update, name = 'update',),
    path( 'contact/<int:contact_id>/delete/', views.delete, name = 'delete',),


# CRUD do modelo Contact 
    # path( 'contact/<int:id_number>/', views.contact_view, name = 'contact',),
    path( 'user/create/', views.register, name='register',),
    path( 'user/login', views.user_login, name = 'login',),
    path( 'user/logout', views.user_logout, name = 'logout',),
    # path( 'user/<int:user_id>/update/', views.user_update, name = 'uupdate',),
    # path( 'contact/<int:contact_id>/delete/', views.delete, name = 'delete',),
]