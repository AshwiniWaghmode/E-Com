from django.shortcuts import render,HttpResponse
from django.contrib import messages
from Shop.models import Register


def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST" :
        Name=request.POST.get('Name')
        Email=request.POST.get('Email')
        password=request.POST.get('password')
        C_pass=request.POST.get('C_pass')
        register=Register(Name=Name,Email=Email,password=password,C_pass=C_pass)
        register.save()
        messages.success(request, 'your msg has been sent....!')
        
    
    #return render(request, 'register.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def category(request):
    return render(request,'category.html')

def popup(request):
    return render(request,'popup.html')

def v_home(request):
    return render(request,'v_home.html')

def art(request):
    return render(request,'art.html')

def craft(request):
    return render(request,'craft.html')