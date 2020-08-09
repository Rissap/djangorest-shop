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


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('id', 'title')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'])

        user.set_password(validated_data['password'])
        user.save()

        return user


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = models.Employee
        fields = ('user', 'post')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data["keys"])



class OrderSerializer(serializers.ModelSerializer):
    sale = SaleSerializer(read_only=True)
    consultant = EmployeeSerializer()
    product = PostSerializer()
    class Meta:
        model = models.Order
        fields = '__all__'