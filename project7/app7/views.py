from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from app7.forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from app7.models import employee
from app7.models import CustomUser
from app7.forms import EmployeeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def signup1(request):
    form = CustomUserCreationForm()
    if (request.method=='POST'):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return home(request)
    return render(request, 'signup1.html',{"form": form})

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

def view(request):
    k=employee.objects.all()
    return render (request,'view.html', {"p":k})

# def add(request):
#     if (request.method=='POST'):
#         id=request.POST['i']
#         nm=request.POST['n']
#         ple=request.POST['p']
#         cpy=request.POST['c']
#         slry=request.POST['s']
#         o=.objects.create(Emp_id=id,Emp_name=nm,place=ple,company_name=cpy,salary=slry)
#         o.save()
#         return view(request)
#     return render (request,'add.html')


def add(request):
    form = EmployeeForm()
    if (request.method=='POST'):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return view(request)
    return render(request, 'add.html',{"form": form})



def delete_emp(request,p):
    s=employee.objects.get(pk=p)
    s.delete()
    return view(request)

def edit_emp(request,p):
    d=employee.objects.get(pk=p)
    form=EmployeeForm(instance=d)
    if (request.method=='POST'):
        form = EmployeeForm(request.POST,instance=d)
        if(form.is_valid()):
            form.save()
            return view(request)
    return render(request,'add.html',{'form':form})