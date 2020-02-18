from django.contrib import admin
from .models import Facture, LigneFacture

# Register your models here.

class FactureInline(admin.StackedInline):
    model = LigneFacture
    can_delete = False
    extra = 1

class FactureAdmin(admin.ModelAdmin):
    inlines = [FactureInline]


admin.site.register(Facture, FactureAdmin)
