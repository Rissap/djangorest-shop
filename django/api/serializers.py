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
		fields = ['id', 'customer', 'consultant', 'product', 'sale', 'created_at']
