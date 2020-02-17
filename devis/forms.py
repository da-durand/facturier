from django.forms import inlineformset_factory
from django import forms
from .models import Devis, LigneDevis

LigneFormSet = inlineformset_factory(Devis, LigneDevis,
    can_delete=False,
    extra= 1,
    fields = ["product", "quantity", "unit_price"],
)


