# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HelloDjango(TemplateView):
    #self.template_name = 'home.html'
    template_name = 'home.html'
    print("get name as ", template_name)