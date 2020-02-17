from django.contrib import admin
from .models import Client, Adress

# Register your models here.

class ClientInline(admin.StackedInline):
    model = Adress
    can_delete = False
    extra = 1

class ClientAdmin(admin.ModelAdmin):
    inlines = [ClientInline]


admin.site.register(Client, ClientAdmin)