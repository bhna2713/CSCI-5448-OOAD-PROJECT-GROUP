from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
class Appointments(models.Model):
	title = models.CharField(max_length = 120)
	Date = models.DateTimeField(auto_now = True, auto_now_add = False)
	Venue = models.CharField(max_length = 120)
	Time = models.CharField(max_length = 120)
	reset =  models.TextField()



	def __unicode__(self):
		return self.title

	def __str__(self):
 		return self.title 

	def get_absolute_url(self):
 		# return reverse("expenses:list" , kwargs={"id": self.id})
 		return "/appointments/list/%s" %(self.id)