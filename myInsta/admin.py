# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myInsta.models import Post, InstaUser
# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)