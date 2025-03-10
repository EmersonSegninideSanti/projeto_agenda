from django.contrib import admin
from contact import models

# Register your models here.

class ContactAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone',)  

admin.site.register(models.Contact, ContactAdmin)