from xml.etree.ElementInclude import default_loader

from django.db import models

class Car(models.Model):
    nameCar = models.CharField(max_length=30)
    priceCar = models.FloatField(blank=True, default=0)
    modelCar = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nameCar, self.priceCar

class Phone(models.Model):
    namePhone = models.CharField(max_length=30,)
    pricePhone = models.IntegerField(max_length=30)
    seria = models.CharField(max_length=30)

    def __str__(self):
        return self.namePhone