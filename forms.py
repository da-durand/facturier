from django.forms import inlineformset_factory
from django import forms
from .models import Client, Adress

ClientFormSet = inlineformset_factory(Client, Adress,
    can_delete=False,
    extra= 1,
    max_num=1)