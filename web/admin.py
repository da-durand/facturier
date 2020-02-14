from django.contrib import admin
from .models import Client, Adress

# Register your models here.

class ClientInline(admin.StackedInline):
    model = Adress
    can_delete = False

class ClientAdmin():
    inlines = (ClientInline,)

admin.site.register(Client, ClientAdmin)