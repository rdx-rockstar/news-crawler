from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 

def home(request):
    return render(request,'home.html',{'user':request.user})

def register(request):
    return render(request,'register.html',{'user':request.user})

def login(request):
    return render(request,'login.html',{'user':request.user})