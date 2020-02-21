from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client
from .forms import AdressFormSet
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin



class ClientCreateView(PermissionRequiredMixin, CreateView):
    model = Client
    template_name = "registration/client_form.html"
    fields = "__all__"
    permission_required = "web.add_client"


    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["client_form"] = AdressFormSet()
        return context


    def form_valid(self, form):

        self.client = form.save(commit = False)
        adress_form = AdressFormSet(self.request.POST, instance = self.client)

        for adress_form_set in adress_form:
            form.save()
            adress_form.save()
        return HttpResponseRedirect(self.get_success_url())

    
    def get_success_url(self):
        return reverse_lazy('client_list') 

class ClientListView(PermissionRequiredMixin, ListView):
    model = Client
    template_name = "parts/client_list.html"
    permission_required = "web.view_client"


class ClientDetailView(PermissionRequiredMixin, DetailView):
    model = Client
    template_name = "parts/client_detail.html"
    slug_field = "adress"
    slug_url_kwarg = "adress"
    permission_required = "web.view_client"


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    model = Client
    template_name = "registration/client_form.html"
    fields = "__all__"
    permission_required = "web.change_client"


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

class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    model = Client
    success_url= reverse_lazy('client_list')
    permission_required = "web.delete_client"
