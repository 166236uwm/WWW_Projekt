from api.serializers import UsersSerializer, ProductSerializer, RecipeSerializer, TransactionSerializer, DeliverySerializer
from projektWWW.models import Users, Product, Recipe
import pytest

def test_users_serializer():
    data = {"username": "test_user", "name": "Test Name", "role": "admin"}
    serializer = UsersSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["username"] == "test_user"

def test_product_serializer():
    data = {"productName": "Milk", "pricePerUnit": 2.5}
    serializer = ProductSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["pricePerUnit"] == 2.5

def test_recipe_serializer():
    data = {"recipeName": "Pasta", "description": "Pasta with tomato sauce"}
    serializer = RecipeSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["recipeName"] == "Pasta"


@pytest.mark.django_db
def test_delivery_serializer():
    user = Users.objects.create(name="test_user")
    product = Product.objects.create(productName="test_product", pricePerUnit=50.0)

    data = {
        "recipient": user.id,
        "total_prize": 10.0,
        "product": product.id
    }

    serializer = DeliverySerializer(data=data)
    assert serializer.is_valid(), serializer.errors

    instance = serializer.save()
    assert instance.recipient == user
    assert instance.total_prize == 10.0
    assert instance.product == product

@pytest.mark.django_db
def test_transaction_serializer():
    # Create necessary test instances
    user = Users.objects.create(name="test_user")
    product1 = Product.objects.create(productName="Product 1", pricePerUnit=10.0)
    product2 = Product.objects.create(productName="Product 2", pricePerUnit=15.0)

    # Create recipes with related products
    recipe1 = Recipe.objects.create(recipeName="Recipe 1")
    recipe1.products.add(product1)  # Add product1 to recipe1
    recipe1.recipeproduct_set.create(product=product1, quantity=2)  # Create a RecipeProduct relation

    recipe2 = Recipe.objects.create(recipeName="Recipe 2")
    recipe2.products.add(product2)  # Add product2 to recipe2
    recipe2.recipeproduct_set.create(product=product2, quantity=3)  # Create a RecipeProduct relation

    # Prepare data for the TransactionSerializer
    data = {
        "POS": user.id,  # Primary key of the user
        "content": [recipe1.id, recipe2.id]  # List of recipe primary keys
    }

    # Test serializer validation
    serializer = TransactionSerializer(data=data)
    assert serializer.is_valid(), serializer.errors  # Validate input data

    # Save the serializer and explicitly set the many-to-many relationship after saving
    transaction = serializer.save()  # Save the transaction first

    # Now set the many-to-many relationship
    transaction.content.set([recipe1, recipe2])  # Assign the recipes to the transaction

    # Verify that the transaction's total_prize is calculated correctly
    assert transaction.total_prize == (recipe1.value + recipe2.value)
    assert list(transaction.content.all()) == [recipe1, recipe2]
