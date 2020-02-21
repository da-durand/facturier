from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Facture
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG
from django.contrib.auth.mixins import PermissionRequiredMixin


# Create your views here.

class FactureListView(PermissionRequiredMixin, ListView):
    model = Facture
    template_name = "parts/facture_list.html"
    permission_required = "facture.view_facture"


class FactureDetailView(PermissionRequiredMixin, DetailView):
    model = Facture
    template_name = "parts/facture_detail.html"
    permission_required = "facture.view_facture"


class FacturePdf(WeasyTemplateResponseMixin, FactureDetailView):

    pdf_attachment = False
    pdf_filename = "facture.pdf"
