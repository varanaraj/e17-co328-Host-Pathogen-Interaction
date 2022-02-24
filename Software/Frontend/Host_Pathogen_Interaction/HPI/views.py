from email import message
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homePage(request):
    message="<h1>welcome to Home page</h1>"
    return render(request,'HPI/home.html')