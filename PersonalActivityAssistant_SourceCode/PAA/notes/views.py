from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notes
from .forms import NotesForm
from .forms import FilterForm
from abc import ABCMeta, abstractmethod
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Home Page
def notes(request):

	return HttpResponse("Home")

#form for adding expenses
def notes_add(request):
	form = NotesForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form" : form,

	}

	return render(request, "notes_templates/add_notes.html", context)

# #View for displaying specific expense url : /expenses/list/id

#Iterator Design Pattern


# Applies here

#class iterator()

#	def iterate(self):
		#pass
def notes_list(request, id):
	instance= get_object_or_404(Notes, id=id)
	context = {"title" : instance.title,
				"instance" : instance,
	}
	return render(request, "notes_templates/edited_view.html", context)

# #View for listing all the expenses url:/expenses/detail

def notes_detail(request):
	querylist = Notes.objects.all().order_by("-date") 
	paginator = Paginator(querylist,2)
	page_num = request.GET.get('page',1)

	try :
			page = paginator.page(page_num)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)

	except PageNotAnInteger:
		page = paginator.page(1)

	context = {"page" : page	
	}
	return render(request, "notes_templates/detail_notes.html", context)

# #View for editing expenses url : expenses/id/edit





def notes_edit(request, id=None):
		instance = get_object_or_404(Notes, id=id)
		form = NotesForm(request.POST or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"title" : instance.title,
			"instance" : instance,
			"form" : form,}
		return render(request, "notes_templates/edit_notes.html", context)

# # View for deleting : To delete go to /expenses/id/delete	








def notes_delete(request, id = None):
	instance = get_object_or_404(Notes, id=id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("/notes/detail")
	
#Filter Design Pattern

#Structure -> Uses a Filter Interface
#Concrete classes or filterTypes that implement the Interface
#Class which is called a Filter chain that will allow us to filter by multiple categories
class FilterInterface():

	__metaclass__ = ABCMeta

	@abstractmethod
	def filtertype(self,request):
		pass

#abstract base class
class FilterByTitle(FilterInterface):

	def filtertype(self,request):
		instance = Notes.objects.filter(title = request.POST['SortbyNotename'])
		
		context = {
			
			"instance" : instance,
			}

		return render(request, "notes_templates/filter_title.html", context)
		

class FilterByNote(FilterInterface):
	def filtertype(self,request):
		instance = Notes.objects.filter(note = request.POST['SortbyNote'])
		context = {
				
				"instance" : instance,
				}

		return render(request, "notes_templates/filter_note.html", context)

class FilterOR(FilterInterface):
	def filtertype(self,request):pass

		
class FilterAND(FilterInterface):
	def filtertype(self,request):pass
		

class FilterDemo():
	def demo(self,request):
		a=FilterByTitle()
		b=FilterByNote()
		dict1 = {"title":a.filtertype(request)}#"note":b.filtertype(request)}
		return dict1





def notes_filter_title(request):
	# a=FilterByTitle()
	# return a.filtertype(request)

	x=FilterDemo()
	y= x.demo(request)
	return y["title"]


def notes_filter_note(request):
	b=FilterByNote()
	return b.filtertype(request)
	






