from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reminders
from .forms import RemindersForm
from abc import ABCMeta, abstractmethod

# Home Page
def reminders(request):

	return HttpResponse("Home")

#form for adding expenses
def reminders_add(request):
	form = RemindersForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form" : form,

	}

	return render(request, "reminders_templates/add_reminders.html", context)


# #View for displaying specific expense url : /expenses/list/id
def reminders_list(request, id):
	instance= get_object_or_404(Reminders, id=id)
	#instance= Entry.objects.get(id=id)

	context = {"title" : instance.title,
				"instance" : instance,
	}
	return render(request, "reminders_templates/edited_view.html", context)

# #View for listing all the expenses url:/expenses/detail
#Null object pattern for displaying a default page when query is empty
class AbstractRemindersView():
	__metaclass__ = ABCMeta

	@abstractmethod
	def isNil():
		pass

class QueryExists(AbstractRemindersView):

	def isNil(self,request):
		querylist = Reminders.objects.all().order_by("-date") 

		context = {"querylist" : querylist	
		}
		return render(request, "reminders_templates/detail_reminders.html", context)



class QueryEmpty (AbstractRemindersView):

	def isNil(self,request):
		# return HttpResponse("Home")
		return redirect("/reminders/none")


		# return render(request1, "reminders_templates/reminder_empty_view.html")

class RemindersFactory():

	def reminderFactory(self,request):
		querylist = Reminders.objects.all().order_by("-date") 
		if querylist.count() == 0:
			emp = QueryEmpty()
			return emp.isNil(request)
		else:
			notemp = QueryExists()
			return notemp.isNil(request)


def reminders_detail(request):
	fact = RemindersFactory()
	return fact.reminderFactory(request)


def reminders_none(request):
	# fact = RemindersFactory()
	# return fact.reminderFactory(request)
	return render(request, "reminders_templates/reminder_empty_view.html")


	
# #View for editing expenses url : expenses/id/edit
def reminders_edit(request, id=None):
		instance = get_object_or_404(Reminders, id=id)
		form = RemindersForm(request.POST or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"title" : instance.title,
			"instance" : instance,
			"form" : form,}
		return render(request, "reminders_templates/edit_reminders.html", context)

# # View for deleting : To delete go to /expenses/id/delete	
def reminders_delete(request, id = None):
	instance = get_object_or_404(Reminders, id=id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("/reminders/detail")
	

