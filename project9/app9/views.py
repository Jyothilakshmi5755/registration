from django.shortcuts import render
from app9.forms import bookForm
from app9.models import Book

# Create your views here.

def home(request):
    return render (request,'home.html')

def upload(request):
    form=bookForm()
    if (request.method == 'POST'):
        form = bookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return home(request)
    return render (request,'upload.html',{"form":form})

def show(request):
    k = Book.objects.all()
    return render(request,'show.html',{"s":k})