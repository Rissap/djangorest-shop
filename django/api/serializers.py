from django.contrib.auth.models import User
from rest_framework import serializers
from main import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price']


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sales
        fields = ['types', 'coef']


class OrderSerializer(serializers.ModelSerializer):
    sale = SaleSerializer(read_only=True)
    class Meta:
        model = models.Order
        fields = ['id', 'customer', 'consultant', 'product', 'total', 'sale', 'confirmed', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Employee
        fields = ('user', 'post')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user