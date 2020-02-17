from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Devis

# Create your views here.
class DevisListView(ListView):
    model = Devis
    template_name = "parts/devis_list.html"

class DevisDetailView(DetailView):
    model = Devis
    template_name = "parts/devis_detail.html"

