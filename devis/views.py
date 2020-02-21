from django.shortcuts import render
from django.conf import settings
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Devis
from facture.models import Facture
from .forms import LigneFormSet
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin

from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG

# Create your views here.
class DevisListView(PermissionRequiredMixin, ListView):
    model = Devis
    template_name = "parts/devis_list.html"
    permission_required = "devis.view_devis"

class DevisDetailView(PermissionRequiredMixin, DetailView):
    model = Devis
    template_name = "parts/devis_detail.html"
    permission_required = "devis.view_devis"


class DevisPdf(WeasyTemplateResponseMixin, DevisDetailView):

    pdf_attachment = False
    pdf_filename = "devis.pdf"

    def __init__(header_html=None, footer_html=None):
        self.header_html = header_html
        self.footer_html = footer_html


class DevisCreateView(PermissionRequiredMixin, CreateView):
    model = Devis
    template_name = "parts/form_devis.html"
    fields = ["client"]
    permission_required = "devis.add_devis"


    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['ligne_form'] = LigneFormSet()
        return context

    def form_valid(self, form):
        self.devis = form.save(commit = False)
        ligne_form = LigneFormSet(self.request.POST, instance = self.devis)
        for form_set in ligne_form :
            form.save()
            form_set.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('devis_list')

class DevisUpdateView(PermissionRequiredMixin, UpdateView):
    model = Devis
    template_name = "parts/form_devis.html"
    fields = "__all__"
    permission_required = "devis.change_devis"


    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context["ligne_form"] = LigneFormSet(instance = self.get_object())
        return context


    def form_valid(self, form):
        self.ligne = form.save(commit = False)
        ligne_form = LigneFormSet(self.request.POST, instance = self.ligne)
        form.save()
        ligne_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('devis_list')

    
class DevisDeleteView(PermissionRequiredMixin, DeleteView):
    model = Devis
    success_url = reverse_lazy('devis_list')
    permission_required = "devis.delete_devis"


class FactureTransformView(PermissionRequiredMixin ,DetailView):
    model = Devis
    template_name = "parts/devis_detail.html"
    permission_required = "devis.add_facture"

    def get(self, request, *args, **kwargs):


        fact = Facture.objects.create(
            devis = self.get_object(),
            client = self.get_object().client
        )
        return HttpResponseRedirect(reverse_lazy("facture_list"))
