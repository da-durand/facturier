# Generated by Django 3.0.3 on 2020-02-17 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0002_devis_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devis',
            name='htc',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='ttc',
        ),
        migrations.RemoveField(
            model_name='lignedevis',
            name='total_unit_price',
        ),
    ]
