from django.shortcuts import render
from django.urls import path
from . import views 
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate
from django.contrib import messages
import requests
from .models import Feeds
from comment.models import Comments
from django import forms
from .forms import FeedForm

# Create your views here.
def feed(request):
    if request.user.is_authenticated:
        # response = requests.get('https://sbuf52bt6i.execute-api.us-east-2.amazonaws.com/Test/drax-test?type=posts')
        # postdata=response.json()
        # print(postdata)
        if request.method=='POST':

            comment=request.POST['Comment']
            PostID=request.POST['PostID']
            UserID=request.user.id
            print(UserID)

            mycomment=Comments.objects.create(Comment=comment, PostID=PostID, UserID_id=UserID)
            mycomment.save()

            return redirect('feed')
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


        if request.method=='POST':

            comment=request.POST['Comment']
            PostID=request.POST['PostID']
            UserID=request.user.id
            print(UserID)

            mycomment=Comments.objects.create(Comment=comment, PostID=PostID, UserID_id=UserID)
            mycomment.save()

            return redirect(reverse('singlefeed') + '?Post='+PostID)
        else:
            PostID=request.GET.get('Post')
            feed=Feeds.objects.get(pk=PostID)
            comment=Comments.objects.filter(PostID=PostID).order_by('-DateTime')
            context={
                'feed':feed,
                'comment':comment
            }
            return render(request,'feeds/singlefeed.html',context)
    else:
        return redirect('login')
def createfeed(request):

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = FeedForm(request.POST, request.FILES)
            if form.is_valid():
                newpost=form.save(commit=False)
                newpost.UserID_id=request.user.id
                newpost.save()
                return redirect('createfeed')
            else:
                print("Form didn't validate")
                return redirect('createfeed')
        else:
            form = FeedForm()
            return render(request, 'feeds/createfeed.html', {
            'form': form
            })
            
    else:
        return redirect('login')
    
