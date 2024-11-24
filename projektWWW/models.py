from django.db import models

#mamy GET i POST
class Users(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

#mamy GET i POST
class Product(models.Model):
    productName = models.CharField(max_length=100)
    pricePerUnit = models.FloatField()

    def __str__(self):
        return self.productName

#mamy GET i POST
class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    products = models.ManyToManyField(Product, through='RecipeProduct')

    @property
    def value(self):
        return sum(
            recipe_product.product.pricePerUnit * recipe_product.quantity
            for recipe_product in self.recipeproduct_set.all()
        )

    def __str__(self):
        return self.recipeName

class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.productName} - {self.quantity}"

#mamy GET i POST
class Transaction(models.Model):
    POS = models.ForeignKey(Users, on_delete=models.CASCADE)
    total_prize = models.FloatField(default=0.0)
    content = models.ManyToManyField(Recipe)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if not is_new:
            self.total_prize = sum(recipe.value for recipe in self.content.all())
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.id}"


class Delivery(models.Model):
    deliveryDate = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(Users, on_delete=models.CASCADE)
    total_prize = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Delivery {self.id}"
