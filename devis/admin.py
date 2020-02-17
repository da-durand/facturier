from django.contrib import admin
from .models import Devis, LigneDevis

# Register your models here.

class DevisInline(admin.ModelAdmin):
    model = LigneDevis
    can_delete = False
    extra = 1

class DevisAdmin(admin.ModelAdmin):
    inlines = [DevisInline]

admin.site.register(Devis, DevisAdmin)