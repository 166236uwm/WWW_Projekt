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