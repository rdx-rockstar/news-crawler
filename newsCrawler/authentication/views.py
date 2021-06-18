from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth 


def home(request):
    return render(request,'home.html',{'user':request.user})

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        if(User.objects.filter(username=username).exists()):
            print('username taken')   
        elif(User.objects.filter(email=email).exists()):
            print('email taken')   
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save();
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
        else:
            print("incorrect credentials")
        return redirect('/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')