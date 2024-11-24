import pytest
from rest_framework.test import APIClient
from django.utils import timezone
from datetime import timedelta
from projektWWW.models import Users, Product, Recipe, Transaction, RecipeProduct

@pytest.mark.django_db
def test_get_products():
    client = APIClient()
    Product.objects.create(productName="Milk", pricePerUnit=2.5)
    response = client.get("/productGet")
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["productName"] == "Milk"

@pytest.mark.django_db
def test_add_product():
    client = APIClient()
    data = {"productName": "Milk", "pricePerUnit": 2.5}
    response = client.post("/productAdd", data)
    assert response.status_code == 200
    assert Product.objects.count() == 1

@pytest.mark.django_db
def test_trn_summary():
    client = APIClient()

    # Create necessary test instances
    user = Users.objects.create(name="test_user")
    product1 = Product.objects.create(productName="Product 1", pricePerUnit=10.0)
    product2 = Product.objects.create(productName="Product 2", pricePerUnit=15.0)

    recipe1 = Recipe.objects.create(recipeName="Recipe 1")
    recipe1.products.add(product1)
    recipe1.recipeproduct_set.create(product=product1, quantity=2)

    recipe2 = Recipe.objects.create(recipeName="Recipe 2")
    recipe2.products.add(product2)
    recipe2.recipeproduct_set.create(product=product2, quantity=3)

    transaction1 = Transaction.objects.create(POS=user, total_prize=35.0)
    transaction1.content.set([recipe1, recipe2])

    transaction2 = Transaction.objects.create(POS=user, total_prize=25.0)
    transaction2.content.set([recipe1])

    start_date = (timezone.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    end_date = (timezone.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    response = client.get(f"/trnSummary?start_date={start_date}&end_date={end_date}")
    assert response.status_code == 200
    assert response.data['total_transactions'] == 2
    assert response.data['average_total_prize'] == 30.0
    assert response.data['sum_total_prize'] == 60.0

@pytest.mark.django_db
def test_trn_summary_invalid_dates():
    client = APIClient()

    start_date = (timezone.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    end_date = (timezone.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    response = client.get(f"/trnSummary?start_date={start_date}&end_date={end_date}")
    assert response.status_code == 400
    assert response.data['error'] == "start_date must be before end_date"

@pytest.mark.django_db
def test_trn_summary_future_end_date():
    client = APIClient()

    user = Users.objects.create(name="test_user")
    product1 = Product.objects.create(productName="Product 1", pricePerUnit=10.0)
    recipe1 = Recipe.objects.create(recipeName="Recipe 1")
    recipe1.products.add(product1)
    recipe1.recipeproduct_set.create(product=product1, quantity=2)

    transaction = Transaction.objects.create(POS=user, total_prize=20.0)
    transaction.content.set([recipe1])

    start_date = (timezone.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    end_date = (timezone.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    response = client.get(f"/trnSummary?start_date={start_date}&end_date={end_date}")
    assert response.status_code == 200
    assert response.data['total_transactions'] == 1
    assert response.data['average_total_prize'] == 20.0
    assert response.data['sum_total_prize'] == 20.0

@pytest.mark.django_db
def test_product_usage_summary():
    client = APIClient()

    product1 = Product.objects.create(productName="Ser", pricePerUnit=2.5)
    product2 = Product.objects.create(productName="Bułka", pricePerUnit=3.0)

    recipe = Recipe.objects.create(recipeName="Kanapka")
    RecipeProduct.objects.create(recipe=recipe, product=product1, quantity=2)
    RecipeProduct.objects.create(recipe=recipe, product=product2, quantity=3)

    user = Users.objects.create(username="pos1", name="POS User", role="cashier")
    transaction = Transaction.objects.create(POS=user)
    transaction.content.add(recipe)

    transaction.created_at = timezone.now() - timedelta(days=1)
    transaction.save()

    start_date = (timezone.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    end_date = timezone.now().strftime("%Y-%m-%d")
    url = f"/productUsageSummary?start_date={start_date}&end_date={end_date}"

    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 2
    assert response.data[0]["product"] == "Bułka"
    assert response.data[0]["total_quantity"] == 3