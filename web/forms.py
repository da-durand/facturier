from django.forms import inlineformset_factory
from django import forms
from .models import Client, Adress

AdressFormSet = inlineformset_factory(Client, Adress,
    can_delete=False,
    extra= 1,
    max_num=3,
    fields = ["adress", "city", "postal_code"],
)