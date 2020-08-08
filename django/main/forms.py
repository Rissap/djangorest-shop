from django import forms
from django.contrib.auth.models import User

from . import models

class UserRegisterForm(forms.ModelForm):
	post = forms.ChoiceField(choices=models.Employee.objects.all(), required=False)

	class Meta:
		model = User
		fields = ["username", "password"]