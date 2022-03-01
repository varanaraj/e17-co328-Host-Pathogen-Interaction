from fileinput import filename
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CreateUserForm
from .models import Collection
from .models import CSVFile

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


def collections(request):
    if(request.method=="POST"):
        id = request.POST.get('id')
        name = request.POST.get('name')

        if(id==""):
            coll = Collection(collectionName=name,userId=request.user)
            coll.save()
            return redirect('Collections')

        coll = Collection.objects.filter(
            id=request.POST.get('id')).update(collectionName=name)
        return redirect('Collections')
        # coll.update(collectionName=request.POST.get('name'))
    coll = Collection.objects.filter(userId=request.user.id)
    return render(request,'bioweb/collections.html',{"collection":coll})


def collDelete(request,id):
    coll=Collection.objects.get(id=id)
    coll.delete()
    return redirect('Collections')


# csv view 

def csvView(request,id):
    url='/csvviews/'+str(id)
    collectionNo = id
    if(request.method == "POST"):
        id = request.FILES
        myfile = request.FILES['myfile']
        print(myfile.name)
        collectionInstance=Collection.objects.get(id=collectionNo)
        newFile = CSVFile(fileName=myfile.name.split(
            ".")[0], collectionId=collectionInstance, csvFile=myfile)
        newFile.save()
        return redirect(url)

        # coll.update(collectionName=request.POST.get('name'))
    # print(id)
    csvfiles = CSVFile.objects.filter(collectionId=collectionNo)
    # print(csvfiles[0].fileName)
    return render(request,'bioweb/csvviews.html',{"csvviews":csvfiles})