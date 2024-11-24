from datetime import datetime
from django.db.models import Count, Avg, Sum
from django.utils import timezone
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