from django.contrib import admin
from . import models


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('user', 'post')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'created_at', 'updated_at')


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('customer', 'product', 'consultant', 'sale', 'total', 'confirmed', 'paid')
	list_filter = ('product', 'customer')


@admin.register(models.Sales)
class SalesAdmin(admin.ModelAdmin):
	list_display = ('types', 'coef', 'priority')
	ordering = ('priority',)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')