from django import forms

from .models import Reminders

class RemindersForm(forms.ModelForm):
	class Meta:
		model = Reminders
		fields = [
			"title",
			"content",
			"time"

		]