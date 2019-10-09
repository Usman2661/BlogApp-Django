from django.shortcuts import render

# Create your views here.
def feed(request):
    return render(request,'feeds/feed.html')
def singlefeed(request):
    return render(request,'feeds/singlefeed.html')
def createfeed(request):
    return render(request,'feeds/createfeed.html')
