from django.contrib import admin
from .models import  About, Service, Blog, Contact, Category

# Register your models here.
class aboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile','email')

admin.site.register(About,aboutAdmin)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Contact)

