# Generated by Django 3.0.3 on 2020-02-18 10:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0003_auto_20200217_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devis',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]