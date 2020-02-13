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
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ClientCreateView.as_view(), name='client_create' ),
    path("clients/", ClientListView.as_view(), name ='client_list'),
    path("client/<int:pk>/", ClientDetailView.as_view(), name = 'client_detail'),
    path("client/<int:pk>/update", ClientUpdateView.as_view(), name = 'client_update'),
    path("client/<int:pk>/delete", ClientDeleteView.as_view(), name = 'client_delete'),
]