from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientFormSet


class ClientCreateView(CreateView):
    model = Client
    template_name = "registration/client_form.html"
    fields = "__all__"
    success_url= reverse_lazy('client_list')

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["client_form"] = ClientFormSet()
        context['tags'] = Tags.objects.all()
        return context

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
    success_url= reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    success_url= reverse_lazy('client_list')

