# Generated by Django 4.1.7 on 2023-05-08 00:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0011_alter_produit_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='dateCde',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]
