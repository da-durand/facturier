from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client
from .forms import AdressFormSet
from django.http import HttpResponseRedirect


class ClientCreateView(CreateView):
    model = Client
    template_name = "registration/client_form.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["client_form"] = AdressFormSet()
        return context


    def form_valid(self, form):
        self.client = form.save(commit = False)
        adress_form = AdressFormSet(self.request.POST, instance = self.client)
        form.save()
        adress_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('client_list') 

class ClientListView(ListView):
    model = Client
    template_name = "parts/client_list.html"


class ClientDetailView(DetailView):
    model = Client
    template_name = "parts/client_detail.html"
    slug_field = "adress"
    slug_url_kwarg = "adress"

class ClientUpdateView(UpdateView):
    model = Client
    template_name = "registration/client_form.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context["client_form"] = AdressFormSet(instance = self.get_object())
        return context


    def form_valid(self, form):
        self.client = form.save(commit = False)
        adress_form = AdressFormSet(self.request.POST, instance = self.client)
        form.save()
        adress_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('client_list') 

class ClientDeleteView(DeleteView):
    model = Client
    success_url= reverse_lazy('client_list')