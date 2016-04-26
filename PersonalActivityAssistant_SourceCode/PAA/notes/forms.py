from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = [
			"title",
			"note"

		]

class FilterForm(forms.ModelForm):
	class Meta:
		model = Notes
		fields = [
			"title",
		

		]



	def clean_recipients(self):
			raise ValidationError("You have forgotten about Fred!")
	