from datetime import datetime
from django.db.models import Count, Avg, Sum
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import  *
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework import status


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

@api_view(['DELETE'])
def deleteUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        serializer = UsersSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateUser(request, pk):
    try:
        user = Users.objects.get(pk=pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Users.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)

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

@api_view(['DELETE'])
def deleteProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['DELETE'])
def deleteRecipe(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return Response({"message": "Recipe deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateRecipe(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Recipe.DoesNotExist:
        return Response({"error": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['DELETE'])
def deleteTransaction(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
        transaction.delete()
        return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Transaction.DoesNotExist:
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateTransaction(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Transaction.DoesNotExist:
        return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['DELETE'])
def deleteDelivery(request, pk):
    try:
        delivery = Delivery.objects.get(pk=pk)
        delivery.delete()
        return Response({"message": "Delivery deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Delivery.DoesNotExist:
        return Response({"error": "Delivery not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateDelivery(request, pk):
    try:
        delivery = Delivery.objects.get(pk=pk)
        serializer = DeliverySerializer(delivery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Delivery.DoesNotExist:
        return Response({"error": "Delivery not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def trnSummary(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    if not start_date_str or not end_date_str:
        return Response({"error": "start_date and end_date are required"}, status=400)

    try:
        start_date = timezone.make_aware(datetime.strptime(start_date_str, '%Y-%m-%d'))
        end_date = timezone.make_aware(datetime.strptime(end_date_str, '%Y-%m-%d'))
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    if start_date > end_date:
        return Response({"error": "start_date must be before end_date"}, status=400)

    if end_date > timezone.now():
        end_date = timezone.now()

    transactions = Transaction.objects.filter(created_at__range=(start_date, end_date))
    summary = transactions.aggregate(
        total_transactions=Count('id'),
        average_total_prize=Avg('total_prize'),
        sum_total_prize=Sum('total_prize')
    )

    return Response(summary)

@api_view(['GET'])
def productUsageSummary(request):
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    if not start_date_str or not end_date_str:
        return Response({"error": "start_date and end_date are required"}, status=400)

    try:
        start_date = timezone.make_aware(datetime.strptime(start_date_str, '%Y-%m-%d'))
        end_date = timezone.make_aware(datetime.strptime(end_date_str, '%Y-%m-%d'))
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    if start_date > end_date:
        return Response({"error": "start_date must be before end_date"}, status=400)

    if end_date > timezone.now():
        end_date = timezone.now()

    transactions = Transaction.objects.filter(created_at__range=(start_date, end_date))
    recipes = transactions.values_list('content', flat=True)

    product_usage = (
        RecipeProduct.objects.filter(recipe__id__in=recipes)
        .values('product__productName')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('-total_quantity')
    )

    summary = [{"product": item['product__productName'], "total_quantity": item['total_quantity']} for item in product_usage]
    return Response(summary)