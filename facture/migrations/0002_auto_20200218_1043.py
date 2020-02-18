# Generated by Django 3.0.3 on 2020-02-18 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200214_0843'),
        ('devis', '0004_auto_20200218_1015'),
        ('facture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='web.Client'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='devis',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='devis', serialize=False, to='devis.Devis'),
        ),
    ]
