# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from myInsta.forms import CustomUserCreationForm

from django.urls import reverse_lazy

from myInsta.models import Post

# Create your views here.

class HelloDjango(TemplateView):
    #self.template_name = 'home.html'
    template_name = 'index.html'
    print("get name as ", template_name)

class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    login_url = 'login'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'detail.html'

    def post_detail_view(request, primary_key):
        try:
            post = Post.objects.get(pk=primary_key)
        except Post.DoesNotExists:
            raise Http404('Post not exists')
        return render(request, 'detail.html', context={'post': post})

class PostCreateView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = '__all__' #or title/image, in the Post

class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ('title',)

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")