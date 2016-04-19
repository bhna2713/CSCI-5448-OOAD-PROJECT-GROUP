from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
from .forms import AddressForm
from django.core.exceptions import ValidationError


# Home Page
def address(request):

	return HttpResponse("Home")
def address_add(request):

	addval = FacadeValidator()
	return addval.facade_add(request)




#form for adding expenses
class FacadeValidator():

	def facade_add(self,request):
		form =AddressForm(request.POST or None)
		if form.is_valid():
			checkn = ValidateName()
			checkm = ValidateMail()
			checka = ValidateAddress()
			if(checkm.checkmail(request) == True and checka.checkaddress(request) == True and checkn.checkname(request) == True ):
				return HttpResponse("Details exist  - All")
			elif (checkn.checkname(request) == True):
				return HttpResponse("Details exist -  Name already exixts")
			elif(checka.checkaddress(request) == True):
				return HttpResponse("Details exist - Address already Exixts")
			elif(checkm.checkmail(request) == True):
				return HttpResponse("Details exist -  Mail already exists")
	


			instance = form.save(commit = False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"form" : form,

		}

		return render(request, "address_templates/add_address.html", context)


class ValidateMail():

	def checkmail(self,request):
		if (Address.objects.filter(Email = request.POST['Email']).exists()) == True :
			return True


class ValidateName():

	def checkname(self,request):
		if (Address.objects.filter(Name = request.POST['Name']).exists()) == True :
			return True


class ValidateAddress():

	def checkaddress(self,request):
		if (Address.objects.filter(Address = request.POST['Address']).exists()) == True :
			return True


# #View for displaying specific expense url : /expenses/list/id
def address_list(request, id):
	instance= get_object_or_404(Address, id=id)
	context = {"Name" : instance.Name,
				"instance" : instance,
	}
	return render(request, "address_templates/edited_view.html", context)

# #View for listing all the expenses url:/expenses/detail
def address_detail(request):
	querylist = Address.objects.all().order_by("-date") 
	context = {"querylist" : querylist	
	}
	return render(request, "address_templates/detail_address.html", context)

# #View for editing expenses url : expenses/id/edit
def address_edit(request, id=None):
		instance = get_object_or_404(Address, id=id)
		form = AddressForm(request.POST or None, instance=instance)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		context = {
			"Name" : instance.Name,
			"instance" : instance,
			"form" : form,}
		return render(request, "address_templates/edit_address.html", context)

# # View for deleting : To delete go to /expenses/id/delete	
def address_delete(request, id = None):
	instance = get_object_or_404(Address, id=id)
	instance.delete()
	messages.success(request, "successfully deleted")
	return redirect("/address/detail")
	

# def get_data(request):
# 	email = request.POST.get['Email']
# 	return HttpResponse(email)


