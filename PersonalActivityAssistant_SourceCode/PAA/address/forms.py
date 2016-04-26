from django import forms
from .models import Address
from django.forms import CharField
from django.core import validators
from abc import ABCMeta, abstractmethod
from django.core.exceptions import ValidationError



class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = [
			"Name",
			"Number",
			"Email",
			"Address"

			]
	




	def clean_Email(self):
		cd = self.cleaned_data
		Email = cd.get('Email')
		if "edu" not in Email:
			raise forms.ValidationError("Invalid Mail")
		return Email


