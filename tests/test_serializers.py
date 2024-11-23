from api.serializers import UsersSerializer, ProductSerializer, RecipeSerializer, TransactionSerializer, DeliverySerializer

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

def test_transaction_serializer():
    data = {"transactionDate": "2021-10-10", "transactionType": "purchase"}
    serializer = TransactionSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["transactionType"] == "purchase"

def test_delivery_serializer():
    data = {"deliveryDate": "2021-10-10", "recipient": "test_user"}
    serializer = DeliverySerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["recipient"] == "test_user"

