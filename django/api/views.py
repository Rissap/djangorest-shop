from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
	queryset = models.Order.objects.all()
	serializer_class = serializers.OrderSerializer


class OrderDetailsView(generics.RetrieveAPIView):
	queryset = models.Order.objects.all()
	serializer_class = serializers.OrderSerializer


class OrderEnrollView(APIView):
	authentication_classes = (BasicAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def post(self, request, format=None):
		customer = request.POST.get("customer")
		product = get_object_or_404(models.Product, pk=request.POST.get("product_id"))
		sale = request.POST.get("sale")
		if not sale:
			sale = sales.get_sale(product)

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
