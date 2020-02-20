from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Facture
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG

# Create your views here.

class FactureListView(ListView):
    model = Facture
    template_name = "parts/facture_list.html"

class FactureDetailView(DetailView):
    model = Facture
    template_name = "parts/facture_detail.html"

class FacturePdf(WeasyTemplateResponseMixin, FactureDetailView):

    pdf_attachment = False
    pdf_filename = "facture.pdf"