from django.contrib import admin
from . import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('user', 'post')
	search_fields = ('user', 'post')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'updated_at')
	search_fields = ('title', )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('customer', 'product', 'created_at')
	list_filter = ('product', 'customer')
	search_fields = ('product', 'customer')

@admin.register(models.Sales)
class SalesAdmin(admin.ModelAdmin):
	list_display = ('types', 'coef',)