from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth 
from .models import defenceArticle,nonDefenceArticle,AIdefenceArticle,AInonDefenceArticle,unclassiedArticle,article
from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI

def AI(request):
    for item in article.objects.all():
        if(not unclassiedArticle.objects.filter(heading=item.heading).exists()):
            newArticle=AIdefenceArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
            newArticle.save()
        item.delete();
    return JsonResponse({'result':"success"})

def home(request):
    return render(request,'home.html',{'user':request.user})

def clearUnclassified(request):
    unclassiedArticle.objects.all().delete()
    return redirect("/unclassified")

def clearDefence(request):
    defenceArticle.objects.all().delete()
    return redirect("/defence")

def clearNonDefence(request):
    nonDefenceArticle.objects.all().delete()
    return redirect("/nondefence")

def clearAIDefence(request):
    AIdefenceArticle.objects.all().delete()
    return redirect("/AIdefence")

def clearAINonDefence(request):
    AInonDefenceArticle.objects.all().delete()
    return redirect("/AInondefence")

def manual(request):
    for item in article.objects.all():
        if(not unclassiedArticle.objects.filter(heading=item.heading).exists()):
            newArticle=unclassiedArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
            newArticle.save()
        item.delete();
    return JsonResponse({'result':"success"})



scrapyd = ScrapydAPI('http://localhost:6800')
@csrf_exempt
@require_http_methods(['POST', 'GET'])
def fetchArticles(request):
    url = request.GET.get('url', None)
    domain = urlparse(url).netloc  # parse the url and extract the domain
    unique_id = str(uuid4())
    settings = {
        'unique_id': unique_id,  # unique ID for each record for DB
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36',
        # 'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }
    if(url.find("hindustan")!=-1):
        task = scrapyd.schedule('default','icrawler',settings=settings, url=url, domain=domain)
    else:
        task = scrapyd.schedule('default', 'icrawler2',settings=settings, url=url, domain=domain)
    return JsonResponse({'task_id':task, 'unique_id': unique_id})

def status(request):
    task_id = request.GET.get('task_id', None)
    unique_id = request.GET.get('unique_id', None)
    print(task_id)
    if not task_id or not unique_id:
        return JsonResponse({'error': 'Missing args'})
    status = scrapyd.job_status('default', task_id)
    return JsonResponse({'status': status})

def uc_to_df(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=unclassiedArticle.objects.get(pk=idd);
    newArticle=defenceArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})


def uc_to_ndf(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=unclassiedArticle.objects.get(pk=idd);
    newArticle=nonDefenceArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})

def uc_to_del(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=unclassiedArticle.objects.get(pk=idd);
    item.delete();
    return JsonResponse({'result':"success"})


def df_to_uc(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=defenceArticle.objects.get(pk=idd);
    newArticle=unclassiedArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})


def df_to_ndf(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=defenceArticle.objects.get(pk=idd);
    newArticle=nonDefenceArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})


def df_to_del(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=defenceArticle.objects.get(pk=idd);
    item.delete();
    return JsonResponse({'result':"success"})

def ndf_to_uc(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=nonDefenceArticle.objects.get(pk=idd);
    newArticle=unclassiedArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})


def ndf_to_df(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=nonDefenceArticle.objects.get(pk=idd);
    newArticle=defenceArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})

def ndf_to_del(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=nonDefenceArticle.objects.get(pk=idd);
    item.delete();
    return JsonResponse({'result':"success"})

def ai_df_to_ndf(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=AIdefenceArticle.objects.get(pk=idd);
    newArticle=AInonDefenceArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})


def ai_df_to_del(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=AIdefenceArticle.objects.get(pk=idd);
    item.delete();
    return JsonResponse({'result':"success"})

def ai_ndf_to_df(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=AInonDefenceArticle.objects.get(pk=idd);
    newArticle=AIdefenceArticle(heading=item.heading, description=item.description, url=item.url,date=item.date)
    item.delete();
    newArticle.save();
    return JsonResponse({'result':"success"})

def ai_ndf_to_del(request):
    idd=request.GET.get('id',None)
    print("id="+idd);
    item=AInonDefenceArticle.objects.get(pk=idd);
    item.delete();
    return JsonResponse({'result':"success"})



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
    articles=defenceArticle.objects.all()
    return render(request, 'defence.html',{'articles':articles})

def nondefence(request):
    articles=nonDefenceArticle.objects.all()
    return render(request, 'nondefence.html',{'articles':articles})

def AIdefence(request):
    articles=AIdefenceArticle.objects.all()
    return render(request, 'AIdefence.html',{'articles':articles})

def AInondefence(request):
    articles=AInonDefenceArticle.objects.all()
    return render(request, 'AInondefence.html',{'articles':articles})

def unclassified(request):
    articles=unclassiedArticle.objects.all()
    return render(request, 'unclassified.html',{'articles':articles})
