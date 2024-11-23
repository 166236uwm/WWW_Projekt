from django.urls import reverse, resolve
from api.views import getUsers, addUser, getProducts, addProducts, getRecipe, addRecipe, getTransaction, addTransaction, getDelivery, addDelivery

def test_user_get_url():
    path = reverse("userGet")
    assert resolve(path).func == getUsers

def test_user_add_url():
    path = reverse("userAdd")
    assert resolve(path).func == addUser

def test_product_get_url():
    path = reverse("productGet")
    assert resolve(path).func == getProducts

def test_product_add_url():
    path = reverse("productAdd")
    assert resolve(path).func == addProducts

def test_recipe_get_url():
    path = reverse("recipeGet")
    assert resolve(path).func == getRecipe

def test_recipe_add_url():
    path = reverse("recipeAdd")
    assert resolve(path).func == addRecipe

def test_transaction_get_url():
    path = reverse("transactionGet")
    assert resolve(path).func == getTransaction

def test_transaction_add_url():
    path = reverse("transactionAdd")
    assert resolve(path).func == addTransaction
