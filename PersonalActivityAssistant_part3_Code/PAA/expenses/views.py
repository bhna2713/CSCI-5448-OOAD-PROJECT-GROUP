from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Expenses
from .forms import ExpensesForm
import djqscsv
import csv
import xlwt
from django.utils.encoding import smart_str
from abc import ABCMeta, abstractmethod

# Home Page
def expenses(request):

	return HttpResponse("Home")

#form for adding expenses
def expenses_add(request):
	form = ExpensesForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form" : form,

	}

	return render(request, "expenses_templates/add_expenses.html", context)

#View for displaying specific expense url : /expenses/list/id
def expenses_list(request, id):
	instance= get_object_or_404(Expenses, id=id)
	context = {"title" : instance.title,
				"instance" : instance,
	}
	return render(request, "expenses_templates/edited_view.html", context)

#View for listing all the expenses url:/expenses/detail
def expenses_detail(request):
	querylist = Expenses.objects.filter(deleted= "").order_by("-date") 
	context = {"querylist" : querylist	
	}
	return render(request, "expenses_templates/detail_expenses.html", context)

#View for editing expenses url : expenses/id/edit
def expenses_edit(request, id=None):
		instance = get_object_or_404(Expenses, id=id)
		form = ExpensesForm(request.POST or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"title" : instance.title,
			"instance" : instance,
			"form" : form,}
		return render(request, "expenses_templates/edit_expenses.html", context)

# View for deleting : To delete go to /expenses/id/delete	
def expenses_delete(request, id = None):
	instance = get_object_or_404(Expenses, id=id)
	setattr(instance, "deleted","true")
	instance.save() 
	messages.success(request, "successfully deleted")
	return redirect("/expenses/detail")
none = ''
# def expenses_delete(request):
# 	delcom = DeleteExpenseCommand()
# 	return delcom.execute(request)

def expenses_undone(self):
	undocx = UndoExpenseCommand()
	undocx.execute()
	return redirect("/expenses/detail")

def expenses_deleteall(self):
	dele = DeleteExpenseCommand()
	dele.execute()
	return redirect("/expenses/detail")



def expenses_export(request):

	return render(request, "expenses_templates/export_expenses.html")

def export_xls(request):
#context for XL exporting method

	cs = ExportXLS()
	return cs.export_method(request)

def export_csv(request):
	#Context for CSV exporting
	rect = ExportCSV()
	return rect.export_method(request)



def expenses_undolist(request):
	querylistundo = Expenses.objects.filter(deleted= "true").order_by("-date") 
	context = {"querylistundo" : querylistundo	
	}
	return render(request, "expenses_templates/undolist_expenses.html", context)

# def expenses_undone(request, id= None):
# 	# instance = Expenses.objects.filter(deleted= "true").order_by("-date") 
# 	instance = get_object_or_404(Expenses, deleted= 'true')
# 	setattr(instance, "deleted","")
# 	instance.save() 
# 		 # return HttpResponse("restored")
# 	return render(request, "expenses_templates/undone_expenses.html")

		



# This is the stratergy class
class ExportStratergy():
# Class declared as an interface using Python ABC module
	__metaclass__ = ABCMeta
	@abstractmethod
	def export_method(self): pass 


#class for stratergy 1 - Exporting in XL
class ExportXLS(ExportStratergy):
	def export_method(self,request):
		response = HttpResponse(content_type='text/xls')
		response['Content-Disposition'] = 'attachment; filename="somefilename.xls"'
		writer = csv.writer(response)
		writer.writerow([
			smart_str(u"title"),
			smart_str(u"category"),
			])
		querylist = Expenses.objects.all().order_by("-date") 
		for obj in querylist:
			writer.writerow([
				smart_str(obj.title),
				smart_str(obj.category),
				])

			return response



#class for stratergy 2 - Exporting in CSV
class ExportCSV(ExportStratergy):
	def export_method(self,request):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
		writer = csv.writer(response)
		writer.writerow([
			smart_str(u"title"),
			smart_str(u"category"),
			])
		querylist = Expenses.objects.all().order_by("-date") 
		for obj in querylist:
			writer.writerow([
				smart_str(obj.title),
				smart_str(obj.category),
				])

		return response




#Commmand Interface that only contains the execute method
class CommandInterface():
	__metaclass__ = ABCMeta

	
	@abstractmethod
	def execute(self):pass 




#concrete commands classes one for deleting the expenses and the other for undoing


class DeleteExpenseCommand(CommandInterface):
	def execute(self):
		receiver.deleteAll()


class UndoExpenseCommand(CommandInterface):
	def execute(self):
		receiver.undocx()


class ExpenseReceiver():
	
	def deleteAll(self):
		#write logic here 
		# instance = get_object_or_404(Expenses, deleted= 'true')
		# instance.delete()
	 	# return redirect("/expenses/detail")
	 	Expenses.objects.filter(deleted= "true").delete()

	def undocx(self):
		#write logic here
		# instance = Expenses.objects.filter(deleted= "true").order_by("-date") 
		# instance = get_object_or_404(Expenses, deleted= 'true')
		# setattr(instance, "deleted","")
		Expenses.objects.filter(deleted= "true").update(deleted = "")

		# instance.save() 





# class RemoteControl():
# 	def setCommand(self,command):pass	

# 	def press(self):
# 		command.execute()

# def expenses_deleteall(request, id = None):
# 	instance = get_object_or_404(Expenses, deleted= 'true')
# 	instance.delete()
# 	messages.success(request, "successfully deleted")
#  	return redirect("/expenses/detail")

# Creating an instance of the Expenses class
receiver = ExpenseReceiver()