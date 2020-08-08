from django.db import models
from django.conf import settings


class Employee(models.Model):
	STATUS_CHOICES = (
		('consultant', 'Consultant'),
		('cashier', 'Cashier'),
		('booker', 'Booker'),
	)

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	post = models.CharField(max_length=15, choices=STATUS_CHOICES, default='consultant')

	def __str__(self):
		return '{} {}'.format(self.post, self.user.username)


class Product(models.Model):
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=13, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {}'.format(self.title, self.price)

class Sales(models.Model):
	types = models.CharField(max_length=20, unique=True)
	coef = models.DecimalField(max_digits=3, decimal_places=2)
	priority = models.IntegerField(unique=True, null=True)

	def __str__(self):
		return '{}'.format(self.coef)

class Order(models.Model):
	customer = models.CharField(max_length=255)
	consultant = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	sale = models.ForeignKey(Sales, on_delete=models.SET_NULL, blank=True, null=True, default=None)
	total = models.DecimalField(max_digits=13, decimal_places=2)
	confirmed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{} {} with {}'.format(self.customer, self.product, self.sale)