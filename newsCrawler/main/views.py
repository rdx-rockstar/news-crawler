from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth 
from .models import article
from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI

def home(request):
    articles=article.objects.all()
    return render(request,'home.html',{'user':request.user,'articles':articles})

def clear(request):
    article.objects.all().delete()
    return redirect('/')

scrapyd = ScrapydAPI('http://localhost:6800')
@csrf_exempt
@require_http_methods(['POST', 'GET'])
def fetchArticles(request):
    url = request.GET.get('url', None)
    domain = urlparse(url).netloc  # parse the url and extract the domain
    unique_id = str(uuid4())
    settings = {
        'unique_id': unique_id,  # unique ID for each record for DB
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }
    task = scrapyd.schedule('default', 'icrawler',settings=settings, url=url, domain=domain)
    return JsonResponse({'task_id':task, 'unique_id': unique_id})

def status(request):
    task_id = request.GET.get('task_id', None)
    unique_id = request.GET.get('unique_id', None)
    print(task_id)
    if not task_id or not unique_id:
        return JsonResponse({'error': 'Missing args'})
    status = scrapyd.job_status('default', task_id)
    return JsonResponse({'status': status})

def loadArticles(request):
    db=article.objects.all()
    articles=[]
    for i in db:
        articles.append(i.title)
    return JsonResponse({'articles': articles})

#############################
#############################
#############################
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

def defence(request):
    return render(request, 'defence.html')


def nondefence(request):
    return render(request, 'nondefence.html')


def unclassified(request):
    return render(request, 'unclassified.html')