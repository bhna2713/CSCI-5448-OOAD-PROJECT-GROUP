from django.shortcuts import render

# Create your views here.
def home(request):
	title = "Title %s" %(request.user)
	context = { 
		"title" : title
	}

	return (request, "/signup/home.html", context)