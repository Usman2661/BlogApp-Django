from django.shortcuts import render
from django.urls import path
from . import views 
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'accounts/login.html')
def register(request):
    return render(request,'accounts/register.html')