from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from datetime import datetime
from services import sales
from main import models
from . import serializers


class ProductListView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductDetailsView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer



class OrderListView(generics.ListAPIView):
    serializer_class = serializers.OrderSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        employee = models.Employee.objects.get(user=self.request.user)
        employee = employee.post.title
        if employee == "Booker":
            return models.Order.objects.all()
        elif employee == "Consultant":
            return models.Order.objects.filter(confirmed=False)
        else: #cashier
            return models.Order.objects.filter(confirmed=True).filter(paid=False)


class OrderDetailsView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)


class OrderConfirmView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        order = get_object_or_404(
            models.Order, pk=request.POST.get('order_id'))
        order.confirmed = True
        order.save()
        return Response({"confirmed": True})


class OrderEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, format=None):
        customer = request.POST.get("customer")
        product = get_object_or_404(models.Product, pk=request.POST.get("product_id"))
        sale = request.POST.get("sale")
        
        if not sale:
            sale = sales.get_sale(product)
        else:
            pass

        total = product.price
        if sale:
            total *= sale.coef

        order = models.Order(
            customer=customer,
            consultant=models.Employee.objects.get(user=request.user),
            product=product,
            sale=sale,
            total=total)

        order.save()
        return Response({'enrolled': True})


class OrderPaymentView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        employee = get_object_or_404(models.Employee, user=request.user)
        confirm = False
        if employee.post.title == 'Cashier':
            order = get_object_or_404(models.Order, pk=request.POST.get('order_id'), confirmed=True)
            order.paid = True
            order.save()
            confirm = True

        return Response({"payment": confirm})


class OrderFilterView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, from_date, to_date, format=None):
        orders = models.Order.objects\
            .filter(created_at__range=[from_date, to_date])

        args = {"orders": []}
        for order in orders:
            args["orders"].append(serializers.OrderSerializer(order).data)

        return Response(args)


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UserSerializer


class CreateEmployeeView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        employee = models.Employee.objects.values_list('user', flat=True)
        users = User.objects.exclude(id__in=employee)
        args = {
            "posts": [],
            "users": []
            }
        
        for user in users:
            args["users"].append(serializers.UserSerializer(user).data)

        for post in models.Post.objects.all():
            args["posts"].append(serializers.PostSerializer(post).data)

        return Response(args)

    def post(self, request, format=None):
        user = get_object_or_404(User, id=request.POST.get("user"))
        post = get_object_or_404(models.Post, id=request.POST.get("post"))

        employee = models.Employee(user=user, post=post)
        employee.save()

        return Response({'register': True})
