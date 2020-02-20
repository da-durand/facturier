from django.db import models
from web.models import Client
import datetime

# Create your models here.

class Devis(models.Model):
    date = models.DateField(default = datetime.date.today)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="devis", null=True)

    def total_ht(self):
        result = 0
        for ligne in self.ligne_devis.all():
            result += ligne.total_quantity_ht()

        return result

    def tva(self):
        return (self.total_ht() * 20) / 100

    def total_ttc(self):
        return self.total_ht() + self.tva()


class LigneDevis(models.Model):
    devis = models.ForeignKey(Devis, on_delete=models.CASCADE, related_name="ligne_devis")
    product = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_quantity_ht(self):
        return round(self.unit_price * self.quantity, 2)


