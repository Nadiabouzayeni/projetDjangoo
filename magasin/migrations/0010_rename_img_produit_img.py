# Generated by Django 4.1.7 on 2023-03-13 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0009_commande_produits'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='Img',
            new_name='img',
        ),
    ]
