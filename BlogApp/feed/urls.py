from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import redirect, reverse


urlpatterns = [
    path('feed', views.feed, name='feed'),
    path('singlefeed', views.singlefeed, name='singlefeed'),
    path('createfeed', views.createfeed, name='createfeed'),
    # path(r'^createfeed/$', views.createfeed, name='createfeeds'),

]
