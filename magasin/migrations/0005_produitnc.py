# Generated by Django 4.1.7 on 2023-03-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0004_fournisseur_produit_fournisseur'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProduitNC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Duree_garantie', models.CharField(max_length=100)),
            ],
        ),
    ]