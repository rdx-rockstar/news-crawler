from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth 

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        if(password!=password1):
            messages.info(request,'password mismatch')
            print('password mismatch')
            return redirect('register') 
        elif(User.objects.filter(username=username).exists()):
            messages.info(request,'username taken')
            print('username taken') 
            return redirect('register')   
        elif(User.objects.filter(email=email).exists()):
            messages.info(request,'email taken')
            print('email taken')  
            return redirect('register') 
        else:
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save();
            return redirect('login')
    else:
        return render(request,'register.html',{'user':request.user})

def login(request):
    if request.method=='POST':
        print("post login")
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if(user is not None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'incorrect credentials')
            print("not correct credentials")
            return redirect('login')
    else:
        print("get login")
        return render(request,'login.html',{'user':request.user})

def logout(request):
    auth.logout(request)
    return redirect('/')