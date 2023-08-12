from django.shortcuts import render
from django.shortcuts import  HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')