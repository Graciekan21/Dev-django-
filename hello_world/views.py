from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def index(request):
if request.method == "POST" ("You must have POSTed something")
    else:
        return HttpResponse(request.method)
 return HttpRequest
def about_me(request):
    return HttpResponse("This would be the about page")
def index(request):
    return HttpResponse("Hello, world!")