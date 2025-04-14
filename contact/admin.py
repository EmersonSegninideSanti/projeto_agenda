from django.contrib import admin
from contact import models

# Register your models here.

class ContactAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone',)

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Category, CategoryAdmin)