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
    POS = models.IntegerField(blank=False)
    total_prize = models.FloatField(blank=False)
    contents = models.CharField(max_length=500, blank=False)

class Recipe(models.Model):
    productID = models.IntegerField(blank=False)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    pricePerUnit = models.FloatField(blank=False)