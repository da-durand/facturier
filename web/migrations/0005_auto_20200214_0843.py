# Generated by Django 3.0.3 on 2020-02-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200213_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adress',
            old_name='test',
            new_name='adress',
        ),
        migrations.AddField(
            model_name='adress',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='adress',
            name='postal_code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
