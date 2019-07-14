"""InstaDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myInsta.views import HelloDjango, PostView, PostDetailView 
from myInsta.views import PostCreateView, PostUpdateView, PostDeleteView, SignupView
from django.urls import path
urlpatterns = [
    path('', PostView.as_view()),
    path('', HelloDjango.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('make_post/', PostCreateView.as_view(), name='make_post'),
    path('update_post/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', PostDeleteView.as_view(), name='delete_post')      
]