import datetime

from django.shortcuts import get_object_or_404

from main.models import Sales

# if product has a few sales (it's old and deffected), select one with the bigger priority
#PRIORITY = ['deffect', 'old']

def get_sale(product):
	"""Return sales according to the product conditions

	:param order: model object Product
	:return: model object Sales
	"""
	sale = None
	old = datetime.date.today() - product.created_at.date()

	if old.days > 30:
		sale = get_object_or_404(Sales, types='old')

	return sale