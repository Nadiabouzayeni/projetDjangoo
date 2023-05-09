# Generated by Django 4.1.7 on 2023-05-08 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0012_alter_commande_datecde_alter_commande_totalcde'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='dateCde',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='totalCde',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
