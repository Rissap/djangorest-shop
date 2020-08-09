from django.urls import path, re_path
from . import views

app_name = 'product_api'

urlpatterns = [
	path('products/', views.ProductListView.as_view(), name='product_list'),
	path('products/<pk>/', views.ProductDetailsView.as_view(), name='product_details'),

	path('orders/', views.OrderListView.as_view(), name='order_list'),
	path('orders/new/', views.OrderEnrollView.as_view(), name="order_enroll"),
	path('orders/confirm/', views.OrderConfirmView.as_view(), name="order_confirm"),
	path('orders/payment/', views.OrderPaymentView.as_view(), name="order_confirm"),

	path('orders/<pk>/', views.OrderDetailsView.as_view(), name='order_details'),
	path('orders/<from_date>/<to_date>/', views.OrderFilterView.as_view(), name='filter_date'),


]