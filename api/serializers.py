from rest_framework import serializers
from projektWWW.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['username', 'name', 'role', 'password', 'password_confirm']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')

        user = Users.objects.create_user(**validated_data)
        return user

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

