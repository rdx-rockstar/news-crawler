from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 

def home(request):
    return render(request,'home.html',{'user':request.user})