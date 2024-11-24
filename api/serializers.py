from rest_framework import serializers
from projektWWW.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    content = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), many=True)

    class Meta:
        model = Transaction
        fields = ['id', 'POS', 'content', 'total_prize']

    def create(self, validated_data):
        content = validated_data.pop('content')
        transaction = Transaction.objects.create(**validated_data)
        transaction.content.set(content)
        transaction.save()
        return transaction

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'

