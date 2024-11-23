import pytest
from projektWWW.models import Users, Product, Recipe, RecipeProduct, Transaction, Delivery

@pytest.mark.django_db
def test_users_creation():
    user = Users.objects.create(username="test_user", name="Test Name", role="admin")
    assert user.username == "test_user"
    assert user.role == "admin"

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(productName="Milk", pricePerUnit=2.5)
    assert str(product) == "Milk"
    assert product.pricePerUnit == 2.5

@pytest.mark.django_db
def test_recipe_value():
    product1 = Product.objects.create(productName="Egg", pricePerUnit=0.5)
    product2 = Product.objects.create(productName="Flour", pricePerUnit=1.0)
    recipe = Recipe.objects.create(recipeName="Cake")
    RecipeProduct.objects.create(recipe=recipe, product=product1, quantity=3)
    RecipeProduct.objects.create(recipe=recipe, product=product2, quantity=2)
    assert recipe.value == 3 * 0.5 + 2 * 1.0
