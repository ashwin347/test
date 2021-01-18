from django.shortcuts import render
from django.http import HttpResponse
from login.models import userdata
# Create your views here.
def home(request):
    return render(request,'welcome.html')

def admin(request):
    return render(request,'admin.html')

def user(request):
    return render(request,'user.html')

def adm_login(request):
    username=request.GET['username']
    passw=request.GET['password']
    if username!='admin' and passw!='123':
        return render(request,{"data":'username or password incorrect'})
    else:
        return render(request,'adminhome.html',{"data":'login successfull'})



def validate(request):
    username=request.GET['username']
    passw=request.GET['password']
    user=userdata.objects.filter(name=username,password=passw)
    if len(user)==0:
    #if username=='ashwin' and passw=='babu':
        return render(request,'user.html',{"data":'username or password incorrect'})
    else:
        return render(request,'user.html',{"data":'login successfull'})
def signup(request):
    username=request.GET['username']
    passw=request.GET['password']
    entry=userdata(name=username,password=passw)
    entry.save()
    return render(request,'user.html',{"data":'signup successfull'})

