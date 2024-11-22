from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    productName = models.CharField(max_length=100)
    pricePerUnit = models.FloatField()

    def __str__(self):
        return self.productName

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)  # Ilość w przepisie (jeśli planujesz to uwzględnić)
    products = models.ManyToManyField(Product, through='RecipeProduct')  # Relacja wiele do wielu z produktem

    @property
    def value(self):
        # Suma wartości dla wszystkich powiązanych produktów w przepisie, uwzględniając ilość
        return sum(product.pricePerUnit * self.recipeproduct_set.filter(recipe=self).first().quantity for product in self.products)

    def __str__(self):
        return self.recipeName

class RecipeProduct(models.Model):
    """Tabela pomocnicza dla wielu produktów w przepisie."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Ilość danego produktu w przepisie

    def __str__(self):
        return f"{self.product.productName} - {self.quantity}"

class Transaction(models.Model):
    POS = models.ForeignKey(Users, on_delete=models.CASCADE)
    total_prize = models.FloatField(default=0.0)  # Może być obliczane podczas zapisywania
    content = models.ManyToManyField(Recipe)  # Relacja do wielu przepisów
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Obliczamy total_prize na podstawie wartości wszystkich przepisów powiązanych z transakcją
        self.total_prize = sum(recipe.value for recipe in self.content.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.id}"

class Delivery(models.Model):
    deliveryDate = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(Users, on_delete=models.CASCADE)
    total_prize = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Poprawka: musiałeś zmienić z `recipient` na `product`

    def __str__(self):
        return f"Delivery {self.id}"
