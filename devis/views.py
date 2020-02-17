from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Devis
from .forms import LigneFormSet
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
class DevisListView(ListView):
    model = Devis
    template_name = "parts/devis_list.html"

class DevisDetailView(DetailView):
    model = Devis
    template_name = "parts/devis_detail.html"

class DevisCreateView(CreateView):
    model = Devis
    template_name = "parts/form_devis.html"
    fields = "__all__"

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

class DevisUpdateView(UpdateView):
    model = Devis
    template_name = "parts/form_devis.html"
    fields = "__all__"

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

    
class DevisDeleteView(DeleteView):
    model = Devis
    success_url = reverse_lazy('devis_list')
    