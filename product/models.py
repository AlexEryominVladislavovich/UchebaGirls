from xml.etree.ElementInclude import default_loader

from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    nameCar = models.CharField(max_length=30)
    priceCar = models.FloatField(blank=True, default=0)
    modelCar = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nameCar,

class Phone(models.Model):
    namePhone = models.CharField(max_length=30)
    pricePhone = models.FloatField(blank=True, default=0)
    seria = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.namePhone

class Category(models.Model):
    name = models.CharField(max_length=30)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    def str(self):
         return self.user.username