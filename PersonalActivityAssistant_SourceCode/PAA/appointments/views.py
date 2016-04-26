from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Appointments
from .forms import AppointmentsForm

# Home Page
def appointments(request):

	return HttpResponse("Home")

#form for adding expenses
def appointments_add(request):
	form =AppointmentsForm(request.POST or None)

	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form" : form,

	}

	return render(request, "appointments_templates/add_appointments.html", context)

# #View for displaying specific expense url : /expenses/list/id
def appointments_list(request, id):
	instance= get_object_or_404(Appointments, id=id)
	context = {"title" : instance.title,
				"instance" : instance,
	}
	return render(request, "appointments_templates/edited_view.html", context)

# #View for listing all the expenses url:/expenses/detail
def appointments_detail(request):
	querylist = Appointments.objects.filter(reset = "").order_by("-Time") 
	context = {"querylist" : querylist	
	}
	return render(request, "appointments_templates/detail_appointments.html", context)

# #View for editing expenses url : expenses/id/edit
def appointments_edit(request, id=None):
		instance = get_object_or_404(Appointments, id=id)
		form = AppointmentsForm(request.POST or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"tite" : instance.title,
			"instance" : instance,
			"form" : form,}
		return render(request, "appointments_templates/edit_appointments.html", context)

# # View for deleting : To delete go to /expenses/id/delete	
def appointments_delete(request, id = None):
	instance = get_object_or_404(Appointments, id=id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("/appointments/detail")
	


def appointments_reset(request):
	origin1 = AppointmentsCaretaker()
	origin1.setFinal(request)
	return redirect("/appointments/detail")


	# Appointments.objects.filter(reset= "").update(reset = "true")
	# messages.success(request, "successfully deleted")
	# return redirect("/appointments/detail")
	
def appointments_restore(request):

	# Appointments.objects.filter(reset= "true").update(reset = "")
	# messages.success(request, "successfully deleted")
	# return redirect("/appointments/detail")
	origin2 = AppointmentsCaretaker()
	origin2.setInitial(request)
	return redirect("/appointments/detail")
	



# Memento Design Pattern -  For Restoring and Resetting Appointments database.

#For restoring the application data to the original format.

class AppointmentsMemento():

	def initialState(self,request):
		Appointments.objects.filter(reset= "true").update(reset = "")
		# messages.success(request, "successfully deleted")
		return render(request,"appointments_templates/detail_appointments.html")



#Appointment  Originator - Contains the instructions for resetting the application data

class AppointmentsOriginator():

	def finalState(self,request):
		Appointments.objects.filter(reset= "").update(reset = "true")
		# messages.success(request, "successfully deleted")
		return render(request,"appointments_templates/detail_appointments.html")


#Caretaker class

class AppointmentsCaretaker():

	def setInitial(self,request):
		initial = AppointmentsMemento()
		initial.initialState(request)


	def setFinal(self,request):
		final = AppointmentsOriginator()
		final.finalState(request)