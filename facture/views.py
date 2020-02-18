from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Facture

# Create your views here.

class FactureListView(ListView):
    model = Facture
    template_name = "../../facture/templates/parts/facture_list.html"