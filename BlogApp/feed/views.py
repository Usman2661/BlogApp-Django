from django.shortcuts import render
from django.urls import path
from . import views 
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib import messages
import requests
from .models import Feeds

# Create your views here.
def feed(request):
    if request.user.is_authenticated:
        # response = requests.get('https://sbuf52bt6i.execute-api.us-east-2.amazonaws.com/Test/drax-test?type=posts')
        # postdata=response.json()
        # print(postdata)
        if request.method=='POST':
            return

        else:
            feed=Feeds.objects.all().order_by('-DateTime')
            context={
                'feed':feed
            }
            return render(request,'feeds/feed.html',context)
    else:
        return redirect('login')
def singlefeed(request):

    if request.user.is_authenticated:
        return render(request,'feeds/singlefeed.html')
    else:
        return redirect('login')
def createfeed(request):
    if request.user.is_authenticated:
        return render(request,'feeds/createfeed.html')
    else:
        return redirect('login')
    
