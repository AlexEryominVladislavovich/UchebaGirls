# Generated by Django 5.2 on 2025-04-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='priceCar',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
