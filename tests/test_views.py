import pytest
from rest_framework.test import APIClient
from projektWWW.models import Product

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
