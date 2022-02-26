from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'bioweb/indexnew.html')

def home(request):
    return render(request,'bioweb/upload.html')

def upload(request):
    return HttpResponse("<h1>good morning</h1>")