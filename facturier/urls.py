"""facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView
from devis.views import DevisListView, DevisDetailView, DevisCreateView, DevisUpdateView, DevisDeleteView, DevisPdf
from facture.views import FactureListView, FactureDetailView, FacturePdf
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ClientCreateView.as_view(), name='client_create' ),
    path("clients/", ClientListView.as_view(), name ='client_list'),
    path("client/<int:pk>/", ClientDetailView.as_view(), name = 'client_detail'),
    path("client/<int:pk>/update", ClientUpdateView.as_view(), name = 'client_update'),
    path("client/<int:pk>/delete", ClientDeleteView.as_view(), name = 'client_delete'),
    path("devis/", DevisListView.as_view(), name = 'devis_list'),
    path("devis/<int:pk>/", DevisDetailView.as_view(), name = 'devis_detail'),
    path("create_devis/", DevisCreateView.as_view(), name = 'devis_create'),
    path("devis/<int:pk>/update", DevisUpdateView.as_view(), name = 'devis_update'),
    path("devis/<int:pk>/delete", DevisDeleteView.as_view(), name = 'devis_delete'),
    path("devis/<int:pk>/pdf", DevisPdf.as_view(), name = 'pdf'),
    path("factures", FactureListView.as_view(), name = 'facture_list'),
    path("facture/<int:pk>/", FactureDetailView.as_view(), name = 'facture_detail'),
    path("facture/<int:pk>/pdf", FacturePdf.as_view(), name = 'pdf_facture'),
    ]
