from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from app8.forms import CustomUserCreationForm
from app8.models import CustomUser

# Create your views here.

def home(request):
    return render (request,'base.html')

def base(request):
    return render (request,'base.html')

def signup1(request):
    form = CustomUserCreationForm()
    if(request.method=='POST'):
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'signup1.html', {"form":form} )

def user_login1(request):
    if(request.method=="POST"):
        name = request.POST['n']
        password = request.POST['p']
        user = authenticate(username=name, password=password)
        if user:
            login(request,user)

            return home(request)
        else:
            return HttpResponse('invalid ... NO USER FOUND!!!')
    return render(request,'login1.html')

def user_logout1(request):
    logout(request)
    return user_login1(request)