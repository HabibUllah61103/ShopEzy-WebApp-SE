# Generated by Django 5.0.1 on 2024-01-17 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopEzy_App', '0011_alter_cartcontainers_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartcontainers',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'managed': False},
        ),
        migrations.AddField(
            model_name='shoppingcarts',
            name='custid',
            field=models.ForeignKey(blank=True, db_column='CustID', null=True, on_delete=django.db.models.deletion.CASCADE, to='ShopEzy_App.customers'),
        ),
    ]
