from datetime import timezone
from django.db import models

class User(models.Model):

    class Plec(models.IntegerChoices):
        Mezczyzna = 1
        Kobieta = 2
        Inne = 3

    username = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(default=timezone.now)

class Transaction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    POS = models.foreignKey('User', on_delete=models.DO_NOTHING)
    total_prize = models.FloatField(blank=False)
    contents = models.ForeignKey('Recipie', on_delete=models.DO_NOTHING)

class Delivery(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    total_prize = models.FloatField(blank=False)
    contents = models.ForeignKey('Product', on_delete=models.DO_NOTHING)

class Recipe(models.Model):
    productID = models.ForeignKey('Product', on_delete=models.DO_NOTHING)
    prize = models.FloatField(blank=False)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    pricePerUnit = models.FloatField(blank=False)