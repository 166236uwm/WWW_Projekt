from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import  *

@api_view(['GET'])
def getUsers(request):
    person = Users.objects.all()
    serializer = UsersSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addUser(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getProducts(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addProducts(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getRecipe(request):
    recipe = Recipe.objects.all()
    serializer = RecipeSerializer(recipe, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addRecipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getTransaction(request):
    transaction = Transaction.objects.all()
    serializer = TransactionSerializer(transaction, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addTransaction(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getDelivery(request):
    delivery = Delivery.objects.all()
    serializer = DeliverySerializer(delivery, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addDelivery(request):
    serializer = DeliverySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
