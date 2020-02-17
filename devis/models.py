from django.db import models
from web.models import Client


# Create your models here.

class Devis(models.Model):
    date = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="devis", null=True)
    htc = models.DecimalField(max_digits=10, decimal_places=2)
    ttc = models.DecimalField(max_digits=10, decimal_places=2)

class LigneDevis(models.Model):
    devis = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name="ligne_devis")
    product = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
