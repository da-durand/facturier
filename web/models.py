from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length= 50)
    phone = models.IntegerField()
    social_reason = models.CharField(max_length = 500)
    siret = models.CharField(max_length = 100)
    tva_num = models.IntegerField()
    email = models.EmailField(max_length = 254)

class Adress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='adress')
    adress = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
