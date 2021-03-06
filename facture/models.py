from django.db import models
from devis.models import Devis
from web.models import Client
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Facture(models.Model):
    devis = models.OneToOneField(Devis, primary_key=True, on_delete=models.CASCADE, related_name="devis")
    date = models.DateField(default = datetime.date.today)
    client = models.ForeignKey(Client, on_delete= models.SET_NULL, related_name="client", null=True)

    def total_ht(self):
        result = 0
        for ligne in self.ligne_facture.all():
            result += ligne.total_quantity_ht()

        return result

    def tva(self):
        return (self.total_ht() * 20) / 100

    def total_ttc(self):
        return self.total_ht() + self.tva()




class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name="ligne_facture")
    product = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_quantity_ht(self):
        return round(self.unit_price * self.quantity, 2)

@receiver(post_save, sender = Facture)
def save_facture(sender, instance, created, **kwargs):

    if created:
        for obj in instance.devis.ligne_devis.all():
            LigneFacture.objects.create(
                product =  obj.product,
                quantity = obj.quantity,
                unit_price  = obj.unit_price,
                facture = instance
            )

