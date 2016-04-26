from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Create your models here.
class Address(models.Model):
	Name = models.CharField(max_length = 120)
	date = models.DateTimeField(auto_now = True, auto_now_add = False)
	Number = models.CharField(max_length = 120)
	Email = models.CharField(max_length = 120)
	Address = models.TextField()

	def __unicode__(self):
		return self.Name

	

	def __str__(self):
 		return self.Name


	def get_absolute_url(self):
 		# return reverse("expenses:list" , kwargs={"id": self.id})
 		return "/address/list/%s" %(self.id)