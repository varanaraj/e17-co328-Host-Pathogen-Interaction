from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request,'bioweb/indexnew.html')


def register(request):
    if request.method == 'POST':
        name = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            user = User.objects.create_user(
                username=name, email=email, password=password1)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(
                request, 'Your account has been created! You are able to login')
            return redirect('Login')
        else:
            messages.warning(request, 'Password Mismatching...!!!')
            return redirect('Register')
    else:
        form = CreateUserForm()
        return render(request, "bioweb/register.html", {'form': form})
