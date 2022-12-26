from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from Shop.models import Register
import re

def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == "POST" :
        Name=request.POST.get('Name')            
        Email=request.POST.get('Email')
        password=request.POST.get('password')
        
        register=Register(Name=Name,Email=Email,password=password)
        register.save()
        messages.success(request, 'your msg has been sent....!')
        
    
    return render(request, 'register.html')

def login(request):
    #return render(request,'login.html')
    if request.method =='POST':
        # get the post parameters
        loginuname = request.POST["loginuname"]
        loginpassword1=request.POST["loginpassword1"]
        #user = authenticate(Email=loginuname, password=loginpassword1)
        if loginuname==Email and loginpassword1==password:
            messages.success (request,"successfully logged in ")
        else:
            messages.success(request,"something wrong try again later")
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

def painting(request):
    return render(request,'painting.html')

def craft(request):
    return render(request,'craft.html')

def earring(request):
    return render(request,'earring.html')

def necklace(request):
    return render(request,'necklace.html')

def other(request):
    return render(request,'otherj.html')

def plates(request):
    return render(request,'plates.html')

def bowls(request):
    return render(request,'bowls.html')

def wooden(request):
    return render(request,'wooden.html')

def vendorregi(request):
    return render(request,'vendor_regi.html')

def custhome(request):
    return render(request,'app/custhome.html')

def faq(request):
    return render(request,'v_faq.html')