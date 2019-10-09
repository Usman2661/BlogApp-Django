from django.shortcuts import render
from django.urls import path
from . import views 
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib import messages



# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return redirect('feed')
    elif request.method=='POST':

        email=request.POST['email']
        password=request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('feed') 
        else:
            messages.error(request,'email or password not correct')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')
                
def register(request):
    if request.user.is_authenticated:
        return redirect('feed')
  

    elif request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
    
        user = User.objects.create_user(password=password, username=email, first_name=name)
        status=user.save()
        print(status)
        return redirect('login')
    else:
        return render(request,'accounts/register.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect ('login')
    else:
        return
