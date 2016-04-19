from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Expenses(models.Model):
	title = models.CharField(max_length = 120)
	category = models.CharField(max_length = 120)
	date = models.DateTimeField(auto_now = True, auto_now_add = False)
	description = models.TextField()
	deleted =  models.TextField()

	def __unicode__(self):
		return self.title

	def __str__(self):
 		return self.title 

 	def get_absolute_url(self):
 		# return reverse("expenses:list" , kwargs={"id": self.id})
 		return "/expenses/list/%s" %(self.id)
 	def get_absolute_url_delete(self):
 		# return reverse("expenses:list" , kwargs={"id": self.id})
 		return "/expenses/delete/%s" %(self.id)

 	# def get_absolute_url1(self):
 	# 	# return reverse("expenses:list" , kwargs={"id": self.id})
 	# 	return "/expenses/%s/delete/"  %(self.id)

 	# def get_absolute_url1(self):
 	# 	# return reverse("expenses:list" , kwargs={"id": self.id})
 	# 	return "/expenses/%s/edit" %(self.id)


