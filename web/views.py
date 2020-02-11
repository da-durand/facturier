from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Client


class ClientCreateView(CreateView):
    model = Client
    template_name = "registration/client_form.html"

