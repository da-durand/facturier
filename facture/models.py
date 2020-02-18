from django.db import models
from devis.models import Devis
from web.models import Client
import datetime


# Create your models here.

class Facture(models.Model):
    devis = models.OneToOneField(Devis, primary_key=True, on_delete=models.CASCADE, related_name="devis")
    date = models.DateField(default = datetime.date.today)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client", null=True)



class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name="ligne_facture")
    product = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)